from django.db import models
from user.models import *


class Car(models.Model):
    model = models.CharField('Nomi', max_length=50)
    is_local = models.BooleanField('Mahalliy brend', default=False)
    is_truck = models.BooleanField('Yuk mashinasi', default=False)

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'

    def __str__(self):
        return self.model


PERSON_CHOICES = (
    ('E', 'Yuridik shaxs'),
    ('P', 'Jismoniy shaxs'),
)


class AccountStatement(models.Model):
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="E")
    car = models.ForeignKey(Car, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    cert_seriya = models.CharField('Qayd etish guvohnomasi seriyasi', max_length=10)
    cert_number = models.CharField('Qayd etish guvohnomasi raqami', max_length=30)
    date_conclusion_contract = models.DateField('Shartnoma tuzilgan sana')
    engine_number = models.CharField('Dvigitel raqami', max_length=50)
    body_number = models.CharField('Kuzov raqami', max_length=50)
    color = models.CharField('Rangi', max_length=50)
    chassis_number = models.CharField("Shassi raqami", max_length=255, blank=True)
    is_checked = models.BooleanField("Hujjatlarni mosligi tekshirilganligi", default=False)
    is_deleted = models.BooleanField("O'chirib yuborilganligi", default=False)
    technical_inspection = models.BooleanField("YXXB RIB tex ko'rik", default=False)
    organization = models.ForeignKey(Organization, on_delete=models.SET_NULL, null=True, blank=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Hisob ma'lumotnoma"
        verbose_name_plural = "Hisob ma'lumotnomalar"

    def __str__(self):
        return f"{self.cert_seriya}{self.cert_number} "


class AccountStatementDocument(models.Model):
    title = models.CharField("Hujjat nomi", max_length=255)
    file = models.FileField("Hujjat", 'media/document/')
    account_statement = models.ForeignKey(AccountStatement, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Fayl"
        verbose_name_plural = "Fayllar"

    def __str__(self):
        return f"{self.title}"
