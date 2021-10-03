from clickuz.models import Transaction
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from clickuz import ClickUz
from django.shortcuts import redirect, get_object_or_404
from clickuz.views import ClickUzMerchantAPIView
from clickuz import ClickUz
from django.urls import reverse_lazy

from click.models import Order
from reception.telegram_bot import send_message_to_developer
from user.models import User


@login_required
def create_order_url(request):
    try:
        if request.GET:
            amount = request.GET.get('amount')
            user = get_object_or_404(User, id=request.user.id)
            order = Order.objects.create(amount=amount,user=user)
            url = ClickUz.generate_url(order_id=order.id, amount=amount,return_url='http://onless.uz/')

        return redirect(url)
    except:
        messages.error(request, 'Xatolik yuz berdi! Sahifani yangilab qayta urinib ko\'ring!')
        return redirect(reverse_lazy('user:personal_data'))

class OrderCheckAndPayment(ClickUz):
    def check_order(self, order_id: str, amount: str):
        send_message_to_developer('check   order_id ' + order_id + ' ' + 'amount ' + amount)

        if order_id:
            print(order_id, 34)
            try:
                order = get_object_or_404(Order, id=order_id)
                print(amount, 37)
                print(str(order.amount), 38)

                # send_message_to_developer('type ' + type(amount) + ' order-amount ' + type(order.amount))
                if amount == str(order.amount):
                    print(42)
                    return self.ORDER_FOUND
                    send_message_to_developer('ORDER_FOUND')
                else:
                    print(46)
                    send_message_to_developer('INVALID_AMOUNT' + amount + ' ' + order.amount)
                    return self.INVALID_AMOUNT
            except:
                print(50)
                send_message_to_developer('ORDER_NOT_FOUND')
                return self.ORDER_NOT_FOUND

    def successfully_payment(self, order_id: str, transaction: object):
        try:
            order = get_object_or_404(Order, id=order_id)
            order.is_paid = True
            order.save()
            send_message_to_developer('successfully add payment from click: ' + order.amount)
        except Order.DoesNotExist:
            send_message_to_developer('successfully add payment from click, no order object not found: ' + order_id)

class TestView(ClickUzMerchantAPIView):
    VALIDATE_CLASS = OrderCheckAndPayment


def success_order(request):
    send_message_to_developer('success_order')


