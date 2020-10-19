from django.db import models
from django.utils import timezone

from account_statement.models import AccountStatement
from user.models import User

PROCESS_CHOICES =  (
    ("1", "Jarayon"),
    ("2", "Qabul qilish"),
    ("3", "Rad etish"),

)

class Application(models.Model):
    created_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True)
    updated_date = models.DateTimeField(verbose_name='Tahrirlangan vaqti', null=True, blank=True)
    process = models.CharField(choices=PROCESS_CHOICES,max_length=12, verbose_name="Holat", default=1)
    process_sms = models.CharField('Jarayon sababi', max_length=600, blank=True)
    is_payment = models.BooleanField('To\'lov', default=False)
    account_statement = models.ForeignKey(AccountStatement,verbose_name='Hisob ma\'lumotnomasi', on_delete=models.SET_NULL, null=True, blank=True,)
    is_delete = models.BooleanField(default=False)
    file = models.FileField('Ariza',upload_to='applications/', null=True, blank=True)
    is_legal = models.BooleanField(default=False, editable=False)
    password = models.IntegerField(blank=True, null=True)


    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'

    def __str__(self):
        return str(self.id)

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)
