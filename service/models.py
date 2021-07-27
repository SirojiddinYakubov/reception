from django.db import models
from django.utils.translation import ugettext_lazy as _
from user.models import *

# SERVICE_CHOICES = (
#     ('account_statement', 'Hisob ma\'lumotnoma'),
#     ('contract_of_sale', 'Oldi sotdi shartnoma'),
#     ('gift_agreement', 'Xadya shartnoma'),
#     ('registration', 'Ro\'yhatga qo\'yish'),
#     ('de_registration', 'Ro\'yhatdan chiqarish'),
#     ('replace_tp', 'Qayd etish guvohnomasini almashtirish'),
#     ('replace_number_and_tp', 'Davlat raqam belgisi va qayd etish guvohnomasini almashtirish'),
#     ('re_equipment', 'Qayta jihozlash'),
#     ('customs_certificate', 'Bojxona guvohnomasi'),
#
# )



class Service(models.Model):
    title = models.CharField(max_length=200,)
    key = models.CharField(max_length=50,unique=True)
    is_active = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    photo = models.CharField(verbose_name="Foto", blank=True, max_length=255)
    deadline = models.CharField(verbose_name="Muddati", max_length=20, )
    instruction = models.TextField(blank=True)
    document = models.ManyToManyField('Document', related_name='service_document', blank=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)


    def __str__(self):
        return str(self.title)

    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislar'

class Document(models.Model):
    title = models.CharField(max_length=200,)
    created_date = models.DateTimeField(verbose_name=_('Yaratgan vaqti'), default=timezone.now)
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Hujjat'
        verbose_name_plural = 'Hujjatlar'
        ordering = ['-id']

    def __str__(self):
        return f"Document: {self.title}"

ROAD_FUND = 1
ROAD_FUND_HORSE_POWER = 2
INSPECTION = 3
TECHNICAL_PASSPORT = 4
REGISTRATION = 5
RE_REGISTRATION = 6
FINE = 7

STATE_DUTY_TITLE = (
    (ROAD_FUND, 'Yo\'l fondi'),
    (ROAD_FUND_HORSE_POWER, 'Yo\'l fondi ot kuchi'),
    (INSPECTION, 'Texnik ko\'rik'),
    (TECHNICAL_PASSPORT, 'Yangi qayd etish guvohnomasi'),
    (REGISTRATION, 'Ro\'yhatlash'),
    (RE_REGISTRATION, 'Qayta ro\'yhatlash'),
    (FINE, 'Jarima')
)

class StateDuty(models.Model):
    service = models.ForeignKey(Service, verbose_name="Xizmat nomi", on_delete=models.CASCADE, null=True, blank=True,
                                related_name='state_duty_service')
    title = models.IntegerField(choices=STATE_DUTY_TITLE, null=True,blank=True)
    payment = models.IntegerField(verbose_name="To'lovi", default=0)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(default=timezone.now)
    created_user = models.ForeignKey(User,verbose_name='Yaratgan shaxs', on_delete=models.SET_NULL, null=True, blank=True)
    is_paid = models.BooleanField(default=False, verbose_name="To'langan")
    score = models.ForeignKey('StateDutyScore', verbose_name='Hisob raqam', on_delete=models.SET_NULL, related_name="state_duty_score", null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.get_title_display()} : {self.payment} so'm"

    class Meta:
        verbose_name = 'Davlat boj to\'lovi'
        verbose_name_plural = 'Davlat boj to\'lovlari'

class StateDutyPercent(models.Model):
    from application.models import PERSON_CHOICES, PHYSICAL_PERSON
    # service = models.ForeignKey(Service, on_delete=models.CASCADE)
    state_duty = models.CharField(max_length=3,choices=STATE_DUTY_TITLE, null=True)
    person_type = models.IntegerField('Shaxs turi', choices=PERSON_CHOICES,default=PHYSICAL_PERSON, blank=True, null=True)
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
        return f"{self.state_duty} : {self.percent}%"

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
