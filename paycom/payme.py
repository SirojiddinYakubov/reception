from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views import View

from application.models import Application, SHIPPED
from click.models import Order, PAYCOM
from reception import settings
from service.models import AmountBaseCalculation
from user.models import User

from .views import MerchantAPIView
from paycom import Paycom
from paycom import status

from reception.telegram_bot import send_message_to_developer

KEY = settings.PAYCOM_SETTINGS['ACCOUNTS']['KEY']


class CheckOrder(Paycom):
    def check_order(self, amount, account):
        send_message_to_developer(f'amount {amount}')
        order_id = account[KEY]
        amount = amount / 100
        try:
            order = Order.objects.get(id=int(order_id))
            if int(order.amount) != int(amount):
                return status.INVALID_AMOUNT
            return status.ORDER_FOUND
        except Order.DoesNotExist:
            return status.ORDER_NOT_FOND

    def successfully_payment(self, account, transaction, *args, **kwargs):
        order_id = int(account)
        try:
            order = get_object_or_404(Order, id=order_id)
            order.is_paid = True
            order.save()

            if order.application:
                application = Application.objects.filter(id=order.application.id).last()
                if application:
                    application.is_block = False
                    application.save()
                else:
                    send_message_to_developer(f'order application not found. Order id: {order.id}')
            else:
                send_message_to_developer(f'order application not found. Order id: {order.id}')

            send_message_to_developer('successfully add payment from payme : ' + order.amount)
        except Order.DoesNotExist:
            send_message_to_developer(f'successfully add payment from payme, no order object not found: {order_id}')

    def cancel_payment(self, account, transaction, *args, **kwargs):
        send_message_to_developer(f'cancel pay from payme : {int(account)}')


class PayMeView(MerchantAPIView):
    VALIDATE_CLASS = CheckOrder


class CreatePaymeOrder(View):

    def get(self, request, *args, **kwargs):
        try:
            if request.GET:
                amount = int(request.GET.get('amount'))
                if not request.GET.get('application'):
                    return HttpResponse("To'lov amalga oshiriladigan ariza topilmadi!")

                application_id = int(request.GET.get('application'))

                if AmountBaseCalculation.objects.filter(is_active=True):
                    activation_pay = int(AmountBaseCalculation.objects.filter(is_active=True).last().amount * 5 / 100)
                    if amount != activation_pay:
                        messages.error(request,
                                       f"Payme orqali to'lov qilishda xatolik! To'lov summasi {activation_pay} so'mga teng bo'lishi kerak!")
                        return redirect(reverse_lazy('application:application_detail', kwargs={'id': application_id}))

                return_url = request.build_absolute_uri(reverse_lazy('application:application_detail', kwargs={'id': application_id}))
                user = get_object_or_404(User, id=request.user.id)

                order = Order.objects.filter(amount=amount, type=PAYCOM, application_id=application_id).last()
                if not order:
                    order = Order.objects.create(amount=amount, user=user, type=PAYCOM, application_id=application_id)

                if not order.application.is_block:
                    messages.error(request, 'Ushbu ariza allaqachon aktivlashtirilgan!')
                    return redirect(reverse_lazy('application:application_detail', kwargs={'id': application_id}))
                payme = Paycom()
                url = payme.create_initialization(order_id=order.id, amount=order.amount,
                                                  return_url=return_url)
                send_message_to_developer(return_url)
                send_message_to_developer(f"{user}: {request.GET.get('amount')}")
                return redirect(url)
            else:
                return redirect(reverse_lazy('application:applications_list'))
        except Order.DoesNotExist:
            send_message_to_developer(f'error order not found payme service')
            messages.error(request, 'Xatolik yuz berdi! Sahifani yangilab qayta urinib ko\'ring!')
            return redirect(reverse_lazy('user:personal_data'))
