import hashlib
import time

from django.db import models
from django.utils import timezone
from service.models import Service
from user.models import User, PERSON_CHOICES, Section
from django.utils.translation import ugettext_lazy as _
PROCESS_CHOICES =  (
    ("1", _("Jarayon")),
    ("2", _("Qabul qilish")),
    ("3", _("Rad etish")),

)
CRON_COICES = (
    ('1', '3 days inside'),
    ('2', '7 days before'),
    ('3', '7 days after'),
)



class Application(models.Model):
    created_user = models.ForeignKey(User,verbose_name=_('Yaratgan shaxs'), on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name=_('Yaratgan vaqti'), null=True, default=timezone.now)
    updated_date = models.DateTimeField(verbose_name=_('Tahrirlangan vaqti'), null=True, blank=True,default=timezone.now)
    process = models.CharField(choices=PROCESS_CHOICES,max_length=12, verbose_name="Holat", default=1)
    process_sms = models.CharField(_('Holat sababi'), max_length=600, blank=True, default=_("Ko'rib chiqilmoqda"))
    is_payment = models.BooleanField(_("To\'lov qilingan"), default=False)
    service = models.ForeignKey(Service, verbose_name='Xizmat turi', on_delete=models.CASCADE, blank=True, null=True, related_name='application_service')
    person_type = models.CharField(_('Ariza topshiruvchi shaxsi'), choices=PERSON_CHOICES, max_length=3, default="J")
    file_name = models.CharField(max_length=64, unique=True, null=True, blank=True, editable=False)
    password = models.IntegerField(blank=True, null=True, verbose_name=_('Ariza tekshiruv kodi'))
    given_date = models.DateField(_('Berish sanasi'),  blank=True, null=True)
    given_time = models.CharField(_('Berish vaqti'), max_length=10, blank=True, null=True)
    canceled_date = models.DateTimeField(verbose_name=_('Rad etilgan vaqti'), null=True,blank=True)
    is_active = models.BooleanField(default=True)
    is_block = models.BooleanField(default=True)
    cron = models.CharField(choices=CRON_COICES,max_length=15, verbose_name=_("CRON holati"), default=1)
    section = models.ForeignKey(Section, verbose_name=_("Ariza topshirilgan IIB YHXB bo'limi"), on_delete=models.CASCADE, blank=True, null=True, related_name='application_section',)

    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'
        ordering = ['-id']

    def __str__(self):
        return self.service.get_title_display()

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

