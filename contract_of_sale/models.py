import hashlib
import time

from django.db import models

from user.models import *


class ContractOfSale(models.Model):
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    seriya = models.CharField('Oldi sotdi shartnomasi seriyasi va raqami', max_length=10, null=True)
    date_conclusion_contract = models.DateField('Shartnoma tuzilgan sana', null=True)
    organization = models.ForeignKey(Organization,verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True, blank=True)
    car = models.ForeignKey(Car,verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True)
    created_user = models.ForeignKey(User,verbose_name='Yaratdi', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True,  default=timezone.now)


    class Meta:
        verbose_name = "Oldi shartnomasiga asosan avtotransport vositasiga raqam olish"
        verbose_name_plural = "Oldi shartnomasiga asosan avtotransport vositasiga raqam olish"

    def __str__(self):
        if self.seriya:
            return f'Oldi sotdi shartnomasi: {self.seriya}'
        else:
            return f"ERROR CONTRACT OF SALE IS NULL"
