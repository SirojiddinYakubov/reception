import hashlib
import time

from django.db import models
from django.utils import timezone
from service.models import Service
from user.models import User, PERSON_CHOICES

PROCESS_CHOICES =  (
    ("1", "Jarayon"),
    ("2", "Qabul qilish"),
    ("3", "Rad etish"),

)




class Application(models.Model):
    created_user = models.ForeignKey(User,verbose_name='Yaratgan shaxs', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)
    updated_date = models.DateTimeField(verbose_name='Tahrirlangan vaqti', null=True, blank=True,default=timezone.now)
    process = models.CharField(choices=PROCESS_CHOICES,max_length=12, verbose_name="Holat", default=1)
    process_sms = models.CharField('Holat sababi', max_length=600, blank=True)
    is_payment = models.BooleanField('To\'lov qilingan', default=False)
    service = models.ForeignKey(Service, verbose_name='Xizmat turi', on_delete=models.CASCADE, blank=True, null=True, related_name='application_service')
    person_type = models.CharField('Ariza topshiruvchi shaxsi', choices=PERSON_CHOICES, max_length=3, default="J")
    file_name = models.CharField(max_length=64, unique=True, null=True, blank=True, editable=False)
    password = models.IntegerField(blank=True, null=True, verbose_name='Ariza tekshiruv kodi')
    given_date = models.DateField('Berish sanasi',  blank=True, default=timezone.now)
    given_time = models.CharField('Berish vaqti', max_length=10, blank=True, null=True)


    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'

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

