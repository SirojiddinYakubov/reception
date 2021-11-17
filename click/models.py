from django.db import models

from application.models import Application
from service.models import Service
from user.models import *

CLICK = 'click'
PAYCOM = 'paycom'

PAYMENT_SERVICES_CHOICES = (
    (CLICK, 'CLICK'),
    (PAYCOM, 'PAYCOM'),
)


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_order')
    is_paid = models.BooleanField(verbose_name='To\'langanligi', default=False)
    type = models.CharField(max_length=10, choices=PAYMENT_SERVICES_CHOICES, default=1)
    application = models.ForeignKey(Application, on_delete=models.CASCADE, null=True, blank=True)
    amount = models.CharField(max_length=20, verbose_name="Summasi")

