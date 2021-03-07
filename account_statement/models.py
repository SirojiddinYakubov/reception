import hashlib
import os
import time
from uuid import uuid4

from django.db import models

from user.models import *


class AccountStatement(models.Model):
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    seriya = models.CharField('Hisob ma\'lumotnomasi seriyasi va raqami', max_length=10, null=True)
    date_conclusion_contract = models.DateField('Shartnoma tuzilgan sana', null=True)
    organization = models.ForeignKey(Organization,verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True, blank=True)
    car = models.ForeignKey(Car,verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True)
    created_user = models.ForeignKey(User,verbose_name='Yaratdi', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)



    class Meta:
        verbose_name = "Hisob ma'lumotnomasiga asosan transport vositasiga raqam olish"
        verbose_name_plural = "Hisob ma'lumotnomasiga asosan transport vositasiga raqam olish"

    def __str__(self):
        if self.seriya:
            return f'Hisob ma\'lumotnoma: {self.seriya}'
        else:
            return f"ERROR ACCOUNT STATEMENT IS NULL"



# class AccountStatementDocument(models.Model):
#     title = models.CharField("Hujjat nomi", max_length=255)
#     file = models.FileField("Hujjat", 'media/document/account_statement/')
#     account_statement = models.ForeignKey(AccountStatement, on_delete=models.SET_NULL, null=True)
#     pub_date = models.DateTimeField(auto_now_add=True)
#
#     class Meta:
#         verbose_name = "Fayl"
#         verbose_name_plural = "Fayllar"
#
#     def __str__(self):
#         return f"{self.title}"
