from django.db import models

from user.models import *

SERVICE_CHOICES = (
    ('account_statement', 'Hisob ma\'lumotnoma'),
    ('contract_of_sale', 'Oldi sotdi shartnoma'),
    ('gift_agreement', 'Xadya shartnoma'),
    ('registration', 'Ro\'yhatga qo\'yish'),
    ('de_registration', 'Ro\'yhatdan chiqarish'),
    ('replace_tp', 'Qayd etish guvohnomasini almashtirish'),
    ('replace_number_and_tp', 'Davlat raqam belgisi va qayd etish guvohnomasini almashtirish'),
    ('re_equipment', 'Qayta jihozlash'),
    ('customs_certificate', 'Bojxona guvohnomasi'),

)


class Service(models.Model):
    title = models.CharField('Xizmat nomi', max_length=50, choices=SERVICE_CHOICES)
    seriya = models.CharField('Seriya', max_length=50, blank=True)
    contract_date = models.DateField(verbose_name="Shartnoma tuzilgan sana", max_length=50, blank=True, null=True)
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J")
    organization = models.ForeignKey(Organization, verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True,
                                     blank=True)
    car = models.ForeignKey(Car, verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True, related_name='service_car')
    created_user = models.ForeignKey(User, verbose_name='Yaratdi', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)

    def __str__(self):
        return self.get_title_display()

    class Meta:
        verbose_name = 'Xizmat'
        verbose_name_plural = 'Xizmatlar'



STATE_DUTY_TITLE = (
    ('1', 'Yo\'l fondi'),
    ('2', 'Yo\'l fondi ot kuchi'),
    ('3', 'Texnik ko\'rik'),
    ('4', 'Yangi qayd etish guvohnomasi'),
    ('5', 'Ro\'yhatlash'),
    ('6', 'Qayta ro\'yhatlash'),
    ('7', 'Jarima')
)


class StateDutyPercent(models.Model):
    # service = models.CharField(max_length=50, choices=SERVICE_CHOICES, blank=True, null=True)
    state_duty = models.CharField(max_length=20, choices=STATE_DUTY_TITLE, null=True)
    person_type = models.CharField('Shaxs turi', choices=PERSON_CHOICES, max_length=3, default="J", blank=True, null=True)
    car_type = models.ForeignKey(CarType, on_delete=models.SET_NULL, verbose_name='Avtomobil turi', blank=True,null=True)
    car_is_new = models.BooleanField(verbose_name='Avtomobil yangi', default=False)
    is_old_number = models.BooleanField(verbose_name='Avtomobildagi DRB eski', default=False)
    lost_number = models.BooleanField(verbose_name='DRB yo\'qolgan', default=False)
    lost_technical_passport = models.BooleanField(verbose_name='Texnik passport yo\'qolgan', default=False)

    start = models.IntegerField(default=0)
    stop = models.IntegerField(default=0)
    percent = models.FloatField(default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_state_duty_display()} : {self.percent}%"

    class Meta:
        verbose_name = 'Davlat boji foizlari'
        verbose_name_plural = 'Davlat bojlari foizlari'


class StateDutyScore(models.Model):
    state_duty = models.CharField(max_length=20, choices=STATE_DUTY_TITLE)
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    score = models.CharField(verbose_name='Hisob raqami', max_length=30, default=0)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    updated_date = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        if self.region:
            return f"{self.get_state_duty_display()} : {self.region.title} : {self.score}"
        else:
            return f"{self.get_state_duty_display()} : {self.score}"

    class Meta:
        verbose_name = 'Davlat boji hisob raqami'
        verbose_name_plural = 'Davlat bojlari hisob raqamlari'
