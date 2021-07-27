import hashlib
import time

from django.db import models
from django.utils import timezone

from service.models import Service, Document
from user.models import User, Section, Organization, Car
from django.utils.translation import ugettext_lazy as _

PROCESS = 1
SUCCESS = 2
CANCEL = 3

PROCESS_CHOICES =  (
    (PROCESS, _("Jarayon")),
    (SUCCESS, _("Qabul qilish")),
    (CANCEL, _("Rad etish")),

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
    created_user = models.ForeignKey(User,verbose_name=_('Yaratgan shaxs'), on_delete=models.SET_NULL, null=True)
    person_type = models.IntegerField(_('Ariza topshiruvchi shaxsi'), choices=PERSON_CHOICES, default=PHYSICAL_PERSON)
    organization = models.ForeignKey(Organization, verbose_name='Tashkilot', on_delete=models.SET_NULL, null=True,
                                     blank=True)
    process = models.IntegerField(choices=PROCESS_CHOICES,verbose_name="Holat", default=PROCESS)
    process_sms = models.CharField(_('Holat sababi'), max_length=600, blank=True, default=_("Ko'rib chiqilmoqda"))
    is_payment = models.BooleanField(_("To\'lov qilingan"), default=False)
    service = models.ForeignKey(Service, verbose_name='Xizmat turi', on_delete=models.CASCADE, blank=True, null=True, related_name='application_service')

    file_name = models.CharField(max_length=64, unique=True, null=True, blank=True, editable=False)
    password = models.IntegerField(blank=True, null=True, verbose_name=_('Ariza tekshiruv kodi'))
    given_date = models.DateField(_('Berish sanasi'),  blank=True, null=True)
    given_time = models.CharField(_('Berish vaqti'), max_length=10, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=True)
    cron = models.CharField(choices=CRON_COICES,max_length=15, verbose_name=_("CRON holati"), default=1)
    section = models.ForeignKey(Section, verbose_name=_("Ariza topshirilgan IIB YHXB bo'limi"), on_delete=models.CASCADE, blank=True, null=True, related_name='application_section',)

    car = models.ForeignKey(Car, verbose_name='Avtomobil', on_delete=models.SET_NULL, null=True,
                            related_name='service_car')
    created_date = models.DateTimeField(verbose_name=_('Yaratgan vaqti'), null=True, default=timezone.now)
    updated_date = models.DateTimeField(verbose_name=_('Tahrirlangan vaqti'), null=True, blank=True,
                                        default=timezone.now)
    canceled_date = models.DateTimeField(verbose_name=_('Rad etilgan vaqti'), null=True, blank=True)
    document = models.ManyToManyField(Document, related_name='application_document', blank=True)

    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'
        ordering = ['-id']

    def __str__(self):
        if self.service.key:
            return f"Application: {self.service.key}"

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

