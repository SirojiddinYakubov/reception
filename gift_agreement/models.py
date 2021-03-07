import hashlib
import time

from django.db import models

from user.models import *


class GiftAgreement(models.Model):
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    seriya = models.CharField('Xisob ma\'lumotnomasi seriyasi va raqami', max_length=10, null=True)
    date_conclusion_contract = models.DateField('Shartnoma tuzilgan sana', null=True)
    organization = models.ForeignKey(Organization,verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True, blank=True)
    car = models.ForeignKey(Car,verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True)
    created_user = models.ForeignKey(User,verbose_name='Yaratdi', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True,  default=timezone.now)



    class Meta:
        verbose_name = "Xadya shartnomasiga asosan avtotransport vositasiga raqam olish"
        verbose_name_plural = "Xadya shartnomasiga asosan avtotransport vositasiga raqam olish"

    def __str__(self):
        if self.seriya:
            return f'Xadya shartnomasi: {self.seriya}'
        else:
            return f"ERROR GIFT AGREEMENT IS NULL"

