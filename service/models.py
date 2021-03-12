from django.db import models

from user.models import *

SERVICE_CHOICES = (
    ('account_statement', 'Hisob ma\'lumotnoma'),
    ('contract_of_sale', 'Oldi sotdi shartnoma'),
    ('gift_agreement', 'Xadya shartnoma'),
    ('4', 'Meros shartnoma'),
    ('5', 'Ro\'yhatga qo\'yish'),
)

class Service(models.Model):
    title = models.CharField('Xizmat nomi',max_length=50, choices=SERVICE_CHOICES)
    seriya = models.CharField('Seriya',max_length=50)
    contract_date = models.DateField(verbose_name="Shartnoma tuzilgan sana",max_length=50)
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    organization = models.ForeignKey(Organization, verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True,blank=True)
    car = models.ForeignKey(Car, verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True)
    created_user = models.ForeignKey(User, verbose_name='Yaratdi', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'

class StateDutyTitle(models.Model):
    title = models.CharField(verbose_name='Nomi', max_length=200)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Davlat boji'
        verbose_name_plural = 'Davlat bojlari'


class StateDutyPercent(models.Model):
    service = models.CharField(max_length=50, choices=SERVICE_CHOICES)
    state_duty = models.ForeignKey(StateDutyTitle, on_delete=models.SET_NULL, null=True)
    percent = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.service} : {self.state_duty} : {self.percent}%"

    class Meta:
        verbose_name = 'Davlat boji foizlari'
        verbose_name_plural = 'Davlat bojlari foizlari'