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
    seriya = models.CharField('Seriya',max_length=50, blank=True)
    contract_date = models.DateField(verbose_name="Shartnoma tuzilgan sana",max_length=50,blank=True)
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    organization = models.ForeignKey(Organization, verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True,blank=True)
    car = models.ForeignKey(Car, verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True)
    created_user = models.ForeignKey(User, verbose_name='Yaratdi', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)

    def __str__(self):
        return self.get_title_display()

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
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, verbose_name='Avtomobil turi', blank=True, null=True)
    start = models.IntegerField(default=0)
    stop = models.IntegerField(default=0)
    percent = models.IntegerField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.service} : {self.state_duty} : {self.percent}%"

    class Meta:
        verbose_name = 'Davlat boji foizlari'
        verbose_name_plural = 'Davlat bojlari foizlari'


class StateDutyScore(models.Model):
    state_duty = models.ForeignKey(StateDutyTitle, on_delete=models.SET_NULL, null=True)
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True, blank=True)
    score = models.CharField(verbose_name='Hisob raqami',max_length=30, default=0)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    updated_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        if self.region:
            return f"{self.state_duty.title} : {self.region.title} : {self.score}"
        else:
            return f"{self.state_duty.title} : {self.score}"

    class Meta:
        verbose_name = 'Davlat boji hisob raqami'
        verbose_name_plural = 'Davlat bojlari hisob raqamlari'