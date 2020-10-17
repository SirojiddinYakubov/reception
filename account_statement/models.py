import os
from uuid import uuid4

from django.db import models

from user.models import Organization, Car

PERSON_CHOICES = (
    ('Y', 'Yuridik shaxs'),
    ('J', 'Jismoniy shaxs'),
)

def account_statement_rename(instance, filename):
    upload_to = 'account_statement/cert_photo/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.cert_seriya and instance.cert_number:
        filename = f'{instance.cert_seriya} {instance.cert_number}.{ext}'
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class AccountStatement(models.Model):
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    cert_seriya = models.CharField('Xisob ma\'lumotnomasi seriyasi', max_length=10, null=True)
    cert_number = models.CharField('Xisob ma\'lumotnomasi raqami', max_length=30, null=True)
    cert_photo = models.ImageField('Xisob ma\'lumotnomasi surati', upload_to=account_statement_rename, blank=True)
    date_conclusion_contract = models.DateField('Shartnoma tuzilgan sana', null=True)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)


    class Meta:
        verbose_name = "Hisob ma'lumotnoma"
        verbose_name_plural = "Hisob ma'lumotnomalar"

    def __str__(self):
        return f"{self.cert_seriya} {self.cert_number} "


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
