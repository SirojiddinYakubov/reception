import hashlib
import time

from django.db import models
from django.utils import timezone

from account_statement.models import AccountStatement
from contract_of_sale.models import ContractOfSale
from gift_agreement.models import GiftAgreement
from user.models import User, PERSON_CHOICES

PROCESS_CHOICES =  (
    ("1", "Jarayon"),
    ("2", "Qabul qilish"),
    ("3", "Rad etish"),

)

class Service(models.Model):
    account_statement = models.ForeignKey(AccountStatement,verbose_name='Hisob ma\'lumotnomasi', on_delete=models.CASCADE, null=True, blank=True,)
    gift_agreement = models.ForeignKey(GiftAgreement, verbose_name='Xadya shartnomasi', on_delete=models.CASCADE, null=True, blank=True, )
    contract_of_sale = models.ForeignKey(ContractOfSale, verbose_name='Oldi sotdi shartnomasi', on_delete=models.CASCADE, null=True, blank=True, )

    class Meta:
        verbose_name = 'Xizmat turi'
        verbose_name_plural = 'Xizmat turlari'

    def __str__(self):
        if self.account_statement:
            return f'Hisob ma\'lumotnoma: {self.account_statement.seriya}'
        elif self.gift_agreement:
            return f"Xadya shartnomasi: {self.gift_agreement.seriya}"
        elif self.contract_of_sale:
            return f"Oldi sotdi shartnomasi: {self.contract_of_sale.seriya}"
        else:
            return f"ERROR SERIVCE IS NULL"


class Application(models.Model):
    created_user = models.ForeignKey(User,verbose_name='Yaratgan shaxs', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name='Yaratgan vaqti', null=True, default=timezone.now)
    updated_date = models.DateTimeField(verbose_name='Tahrirlangan vaqti', null=True, blank=True,default=timezone.now)
    process = models.CharField(choices=PROCESS_CHOICES,max_length=12, verbose_name="Holat", default=1)
    process_sms = models.CharField('Holat sababi', max_length=600, blank=True)
    is_payment = models.BooleanField('To\'lov qilingan', default=False)
    service = models.ForeignKey(Service, verbose_name='Xizmat turi', on_delete=models.CASCADE, blank=True, null=True)
    is_delete = models.BooleanField(default=False)
    person_type = models.CharField('Ariza topshiruvchi shaxsi', choices=PERSON_CHOICES, max_length=3, default="J")
    file_name = models.CharField(max_length=64, unique=True, null=True, blank=True, editable=False)
    password = models.IntegerField(blank=True, null=True, verbose_name='Ariza tekshiruv kodi')


    class Meta:
        verbose_name = 'Ariza'
        verbose_name_plural = 'Arizalar'

    def __str__(self):
        try:
            if self.service.account_statement:
                return f'Hisob ma\'lumotnoma: {self.service.account_statement.seriya}'
            elif self.service.gift_agreement:
                return f"Xadya shartnomasi: {self.service.gift_agreement.seriya}"
            elif self.service.contract_of_sale:
                return f"Oldi sotdi shartnomasi: {self.service.contract_of_sale.seriya}"
            else:
                return f"{self.id}"
        except AttributeError:
            return f"ERROR APPLICATION IS NULL"

    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()

        if self.file_name is None:
            b = bytes(f"{self.password}{time.time() * 1000}{self.created_date.time()}", encoding='utf-8')
            self.file_name = hashlib.md5(b).hexdigest()[0:15]
        return super().save(*args, **kwargs)
