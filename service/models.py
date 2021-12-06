import datetime
import time

from django.utils.translation import ugettext_lazy as _

from user.base import BaseModel
from user.models import *
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
    short_title = models.CharField(max_length=40)
    long_title = models.CharField(max_length=200)
    key = models.CharField(max_length=50, unique=True)
    is_active = models.BooleanField(default=True)
    desc = models.TextField(blank=True)
    photo = models.CharField(verbose_name="Foto", blank=True, max_length=255)
    deadline = models.CharField(verbose_name="Muddati", max_length=20, )
    instruction = models.TextField(blank=True)
    document = models.ManyToManyField('ExampleDocument', blank=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)
    sort = models.IntegerField(default=1)

    def __str__(self):
        return str(self.short_title)

    class Meta:
        verbose_name = 'Servis'
        verbose_name_plural = 'Servislar'


class ExampleDocument(BaseModel):
    title = models.CharField(max_length=200)
    key = models.CharField(max_length=100, unique=True)

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
TEST = 8
# POLICE_INSPECTION = 8

STATE_DUTY_TITLE = (
    (ROAD_FUND, 'Yo\'l fondi'),
    (ROAD_FUND_HORSE_POWER, 'Yo\'l fondi ot kuchi'),
    (INSPECTION, 'Texnik ko\'rik'),
    (TECHNICAL_PASSPORT, 'Yangi qayd etish guvohnomasi'),
    (REGISTRATION, 'Ro\'yhatlash'),
    (RE_REGISTRATION, 'Qayta ro\'yhatlash'),
    (FINE, 'Jarima'),
    (TEST, "Test uchun"),
)


# Eng kam bazaviy hisoblash miqdori
class AmountBaseCalculation(models.Model):
    amount = models.IntegerField(verbose_name="Miqdori")
    start = models.DateField(blank=True, null=True, verbose_name="Qaysi sanadan kuchga kirgan")
    stop = models.DateField(blank=True, null=True, verbose_name="Qaysi sana kuchini yo'qotgan")
    # is_archive = models.BooleanField(default=False, verbose_name="Arxiv BHM hisoblanadimi?")
    is_active = models.BooleanField(default=False, verbose_name="Hozirda aktivmi?")

    def __str__(self):
        return f"{self.amount}"

    class Meta:
        verbose_name = 'Bazaviy hisoblash miqdori'
        verbose_name_plural = 'Bazaviy hisoblash miqdorlari'


class StateDutyPercent(models.Model):
    from application.models import PERSON_CHOICES, PHYSICAL_PERSON
    title = models.CharField(max_length=255, blank=True, null=True)
    service = models.ManyToManyField("service.Service", blank=True)
    state_duty = models.IntegerField(choices=STATE_DUTY_TITLE, null=True)
    person_type = models.IntegerField(choices=PERSON_CHOICES, default=PHYSICAL_PERSON, blank=True,
                                      null=True)
    car_type = models.ManyToManyField(CarType, blank=True)
    car_is_new = models.BooleanField(default=False)
    is_old_number = models.BooleanField(default=False)
    is_save_old_number = models.BooleanField(default=False)
    is_saved_number = models.BooleanField(default=False)
    lost_number = models.BooleanField(default=False)
    lost_technical_passport = models.BooleanField(default=False)
    is_auction = models.BooleanField(default=False)
    is_tranzit = models.BooleanField(default=False)
    contract_fine = models.BooleanField(default=False)
    is_relative = models.BooleanField(default=False)
    start = models.IntegerField(default=0)
    stop = models.IntegerField(default=0)
    percent = models.FloatField(default=0)

    # created_date = models.DateTimeField(default=timezone.now)
    # updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.get_state_duty_display()}({self.id}) : {self.percent}%"

    class Meta:
        verbose_name = 'Davlat boji foizlari'
        verbose_name_plural = 'Davlat bojlari foizlari'


class StateDutyScore(models.Model):
    state_duty = models.IntegerField(choices=STATE_DUTY_TITLE)
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


class PaidStateDuty(models.Model):
    application = models.ForeignKey("application.Application", on_delete=models.CASCADE, verbose_name="Ariza",
                                    related_name="state_duty_application")
    score = models.ForeignKey(StateDutyScore, on_delete=models.CASCADE, verbose_name="Hisob raqam")
    percent = models.ForeignKey(StateDutyPercent, on_delete=models.CASCADE, verbose_name="Hisob raqam foizlari")
    is_return = models.BooleanField(default=False)
    created_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.application} {self.percent}%"

    class Meta:
        verbose_name = "To'langan bojlar"
        verbose_name_plural = "To'langan bojlar"



class GetPayFromCard(BaseModel):
    from application.models import Application
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    card_number = models.CharField(max_length=16)
    exp_date = models.CharField(max_length=4)
    amount = models.IntegerField(default=0)
    transaction_id = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.application.applicant} {self.amount}%"



KAPITALBANK = 1
ORIENT_FINANS_BANK = 2

PAYMENT_SYSTEM = (
    (KAPITALBANK, 'Kapitalbank'),
    (ORIENT_FINANS_BANK, 'Orient Finans Bank'),
)



class PaymentForTreasury(BaseModel):
    from application.models import Application
    PROCESSING = 'processing'
    SUCCESS = 'success'
    FAILED = 'failed'
    CANCELED = 'canceled'
    STATUS = (
        (PROCESSING, 'processing'),
        (SUCCESS, 'success'),
        (FAILED, 'failed'),
        (CANCELED, 'canceled')
    )

    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    amount = models.IntegerField(default=0)
    state_duty_score = models.ForeignKey(StateDutyScore, on_delete=models.CASCADE)
    state_duty_percent = models.ForeignKey(StateDutyPercent, on_delete=models.CASCADE)
    amount_base_calculation = models.ForeignKey(AmountBaseCalculation, on_delete=models.SET_NULL, null=True)
    memorial = models.URLField(verbose_name="Kvitansiya manzili", blank=True, null=True)
    payment_system = models.IntegerField(choices=PAYMENT_SYSTEM, null=True)
    transaction_id = models.CharField(max_length=255,blank=True, null=True)
    status = models.CharField(choices=STATUS, default=PROCESSING, max_length=55)
    is_send = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.application.applicant} {self.amount}%"


    def save(self, *args, **kwargs):
        if self.transaction_id is None:
            self.transaction_id = int(self.application.id + time.time())
        return super(PaymentForTreasury, self).save(*args, **kwargs)