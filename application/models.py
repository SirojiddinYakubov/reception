from django.db import models
from django.utils import timezone

from account_statement.models import AccountStatement
from user.models import User


class Application(models.Model):
    created_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True)
    updated_date = models.DateTimeField(verbose_name='Tahrirlangan vaqti', null=True, blank=True)
    is_checked = models.BooleanField("Hujjatlarni mosligi tekshirilganligi", default=False)
    account_statement = models.ForeignKey(AccountStatement,verbose_name='Hisob ma\'lumotnomasi', on_delete=models.SET_NULL, null=True, blank=True)
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
