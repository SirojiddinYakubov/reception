from clickuz.models import Transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from clickuz import ClickUz
from django.shortcuts import redirect, get_object_or_404
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz
from django.urls import reverse_lazy
from django.views import View

from api.v1.application.utils import ApplicationSuccessCreatedMessage
from application.models import Application, SHIPPED
from click.models import Order, CLICK
from reception.telegram_bot import send_message_to_developer
from service.models import AmountBaseCalculation
from user.models import User, APP_CREATOR


class CreateClickOrder(View):
    def get(self, request, *args, **kwargs):
        try:
            amount = int(request.GET.get('amount'))
            if not request.GET.get('application'):
                return HttpResponse("To'lov amalga oshiriladigan ariza topilmadi!")

            application_id = int(request.GET.get('application'))

            if AmountBaseCalculation.objects.filter(is_active=True):
                if request.user.role == APP_CREATOR:
                    activation_pay = int(AmountBaseCalculation.objects.filter(is_active=True).last().amount * 6 / 100)
                else:
                    activation_pay = int(AmountBaseCalculation.objects.filter(is_active=True).last().amount * 5 / 100)

                if amount != activation_pay:
                    messages.error(request,
                                   f"Click orqali to'lov qilishda xatolik! To'lov summasi {activation_pay} so'mga teng bo'lishi kerak!")
                    return redirect(reverse_lazy('application:application_detail', kwargs={'id': application_id}))

            return_url = request.build_absolute_uri(reverse_lazy('application:application_detail', kwargs={'id': application_id}))
            user = get_object_or_404(User, id=request.user.id)

            order = Order.objects.filter(amount=amount, type=CLICK, application_id=application_id).last()
            if not order:
                order = Order.objects.create(amount=amount, user=user, type=CLICK, application_id=application_id)

            if not order.application.is_block:
                messages.error(request, 'Ushbu ariza allaqachon aktivlashtirilgan!')
                return redirect(reverse_lazy('application:application_detail', kwargs={'id': application_id}))

            url = ClickUz.generate_url(order_id=order.id, amount=str(order.amount), return_url=return_url)
            send_message_to_developer(return_url)
            send_message_to_developer(f"{user}: {request.GET.get('amount')}")
            return redirect(url)
        except:
            messages.error(request, 'Xatolik yuz berdi! Sahifani yangilab qayta urinib ko\'ring!')
            return redirect(reverse_lazy('user:personal_data'))


class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        send_message_to_developer('check   order_id ' + order_id + ' ' + 'amount ' + amount)

        if order_id:
            try:
                order = get_object_or_404(Order, id=order_id)
                if amount == str(order.amount):
                    return self.ORDER_FOUND
                else:
                    send_message_to_developer('INVALID_AMOUNT: ' + amount + ' : ' + order.amount)
                    return self.INVALID_AMOUNT
            except:
                send_message_to_developer('ORDER_NOT_FOUND')
                return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        try:
            order = get_object_or_404(Order, id=order_id)
            order.is_paid = True
            order.save()

            if order.application:
                application = Application.objects.filter(id=order.application.id).last()
                if application:
                    application.is_block = False
                    application.save()

                    ApplicationSuccessCreatedMessage(application).get()
                else:
                    send_message_to_developer(f'order application not found. Order id: {order.id}')
            else:
                send_message_to_developer(f'order application not found. Order id: {order.id}')

            send_message_to_developer('successfully add payment from click : ' + order.amount)
        except Order.DoesNotExist:
            send_message_to_developer(f'successfully add payment from click, no order object not found: {order_id}')


class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment


def success_order(request):
    send_message_to_developer('success_order')
