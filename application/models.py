import hashlib
import os
import time
from uuid import uuid4

from django.db import models
from django.utils import timezone

from service.models import Service, ExampleDocument
from user.base import BaseModel
from user.models import User, Section, Organization, Car, CHECKER
from django.utils.translation import ugettext_lazy as _

CREATED = 0  # Yaratildi
SHIPPED = 1  # Jo'natildi
ACCEPTED_FOR_CONSIDERATION = 2  # Ko'rib chiqish uchun qabul qilindi
WAITING_FOR_PAYMENT = 3  # To'lovni kutmoqda
WAITING_FOR_ORIGINAL_DOCUMENTS = 4  # Hujjatlarning asl nusxasini kutmoqda
SUCCESS = 5  # Muvaffaqiyatli yakunlandi
REJECTED = 6  # Rad etildi

PROCESS_CHOICES = (
    (CREATED, "Ariza yaratildi"),
    (SHIPPED, "Jo'natildi"),
    (ACCEPTED_FOR_CONSIDERATION, "Ko'rib chiqish uchun qabul qilindi"),
    (WAITING_FOR_PAYMENT, "To'lovni kutmoqda"),
    (WAITING_FOR_ORIGINAL_DOCUMENTS, "Hujjatlarni asl nusxasini kutmoqda"),
    (SUCCESS, "Muvaffaqiyatli yakunlandi"),
    (REJECTED, "Rad etildi"),

)

CRON_COICES = (
    ('1', '3 days inside'),
    ('2', '7 days before'),
    ('3', '7 days after'),
)

PHYSICAL_PERSON = 0
LEGAL_PERSON = 1

PERSON_CHOICES = (
    (LEGAL_PERSON, 'Yuridik shaxs'),
    (PHYSICAL_PERSON, 'Jismoniy shaxs'),
)


class Application(models.Model):
    created_user = models.ForeignKey(User, verbose_name=_('Yaratgan shaxs'), on_delete=models.SET_NULL, null=True,
                                     related_name='user_application')
    person_type = models.IntegerField(_('Ariza topshiruvchi shaxsi'), choices=PERSON_CHOICES, default=PHYSICAL_PERSON)
    organization = models.ForeignKey(Organization, verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True,
                                     blank=True)
    process = models.IntegerField(choices=PROCESS_CHOICES, verbose_name="Holat", default=CREATED)

    is_payment = models.BooleanField(_("To\'lov qilingan"), default=False)
    service = models.ForeignKey(Service, verbose_name='Xizmat turi', on_delete=models.CASCADE, blank=True, null=True,
                                related_name='application_service')

    file_name = models.CharField(max_length=64, unique=True, null=True, blank=True, editable=False)
    password = models.IntegerField(blank=True, null=True, verbose_name=_('Ariza tekshiruv kodi'))
    given_date = models.DateField(_('Berish sanasi'), blank=True, null=True)
    given_time = models.CharField(_('Berish vaqti'), max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=True)
    cron = models.CharField(choices=CRON_COICES, max_length=15, verbose_name=_("CRON holati"), default=1)
    section = models.ForeignKey(Section, verbose_name=_("Ariza topshirilgan IIB YHXB bo'limi"),
                                on_delete=models.CASCADE, blank=True, null=True, related_name='application_section', )

    car = models.ForeignKey(Car, verbose_name='Avtomobil', on_delete=models.CASCADE, null=True,
                            related_name='service_car')
    created_date = models.DateTimeField(verbose_name=_('Yaratgan vaqti'), null=True, default=timezone.now)
    updated_date = models.DateTimeField(verbose_name=_('Tahrirlangan vaqti'), null=True, blank=True,
                                        default=timezone.now)
    canceled_date = models.DateTimeField(verbose_name=_('Rad etilgan vaqti'), null=True, blank=True)
    confirmed_date = models.DateTimeField(verbose_name=_('Tasdiqlangan vaqti'), null=True, blank=True)
    inspector = models.ForeignKey(User, verbose_name=_('Inspektor'), on_delete=models.SET_NULL, null=True, blank=True,
                                  related_name='inspector_application')

    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'
        ordering = ['-id']

    def __str__(self):
        if self.service.key:
            return f"Application({self.id}): {self.service.key}"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()

        if self.file_name is None:
            b = bytes(f"{self.password}{time.time() * 1000}{self.created_date.time()}", encoding='utf-8')
            self.file_name = hashlib.md5(b).hexdigest()[0:15]
        return super().save(*args, **kwargs)


# class Payment(models.Model):

def path_and_rename(instance, filename):
    ext = filename.split('.')[-1]
    filename = '{}.{}'.format(uuid4().hex, ext)
    upload_to = 'application_attachments/' + str(
        instance.application_document.application.service.short_title) + '/' + str(
        instance.application_document.example_document.title)
    return os.path.join(upload_to, filename)


class ApplicationDocument(BaseModel):
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    example_document = models.ForeignKey(ExampleDocument, on_delete=models.SET_NULL, null=True)
    seriya = models.CharField('Seriya', max_length=50, blank=True, null=True)
    contract_date = models.DateField(verbose_name="Shartnoma tuzilgan sana", max_length=50, blank=True, null=True)


class ApplicationDocumentAttachment(BaseModel):
    application_document = models.ForeignKey(ApplicationDocument, on_delete=models.CASCADE)
    attachment = models.FileField(upload_to=path_and_rename)


APPLICATION_ACTIVATION = 0
APPLICATION_STATE_DUTY_PAYMENT = 1

APPLICATION_CASH_BY_MODERATOR_STATUS = (
    (APPLICATION_ACTIVATION, 'Ariza holatini aktivlashtirish'),
    (APPLICATION_STATE_DUTY_PAYMENT, 'Arizaning davlat bojlarini qabul qilish'),
)

class ApplicationCashByModerator(BaseModel):
    status = models.PositiveIntegerField(choices=APPLICATION_CASH_BY_MODERATOR_STATUS)
    application = models.ForeignKey(Application, on_delete=models.SET_NULL, null=True)
    moderator = models.ForeignKey(User, verbose_name=_('Moderator'), on_delete=models.SET_NULL, null=True)
    paid_state_duty = models.ForeignKey('service.PaidStateDuty', on_delete=models.SET_NULL, null=True)