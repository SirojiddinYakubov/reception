from django.db import models
import datetime
import os
from uuid import uuid4
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, PermissionsMixin
from django.http import Http404
from django.urls import reverse
from django.utils import timezone
from django.utils.translation import ugettext_lazy as _
from django.core.validators import MaxValueValidator, MinValueValidator, MinLengthValidator, MaxLengthValidator


from reception import settings


class Region(models.Model):
    title = models.CharField('Nomi', max_length=255)
    sort = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', ]
        verbose_name = 'Viloyat'
        verbose_name_plural = 'Viloyatlar'


class District(models.Model):
    title = models.CharField('Nomi', max_length=255)
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True)
    sort = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', ]
        verbose_name = 'Tuman/Shahar'
        verbose_name_plural = 'Tumanlar/Shaharlar'


class MFY(models.Model):
    title = models.CharField('Nomi', max_length=255)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True)
    sort = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', ]
        verbose_name = 'Mahalla'
        verbose_name_plural = 'Mahallalar'


# class Nationality(models.Model):
#     title = models.CharField('Nomi', max_length=255)
#     sort = models.IntegerField(blank=True, default=1)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         ordering = ['sort', ]
#         verbose_name = 'Millat'
#         verbose_name_plural = 'Millatlar'


ROLE_CHOICES = (
    ("1", "User"),
    ("2", "R.I.B"),
    ("3", "M.I.R.B"),

)

# GENDER_CHOICES = (
#     ('M', 'Erkak'),
#     ('W', 'Ayol'),
# )

def path_and_rename(instance, filename):
    upload_to = 'passport_photos/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.phone:
        filename = '{}.{}'.format(instance.phone, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class User(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField('Familiya', max_length=255, blank=True)
    first_name = models.CharField('Ism', max_length=255, blank=True)
    middle_name = models.CharField('Otasining ismi', max_length=255, blank=True)
    role = models.CharField('Foydalanuvchi roli', choices=ROLE_CHOICES, max_length=15, default="1")
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    mfy = models.ForeignKey(MFY, on_delete=models.SET_NULL, verbose_name='MFY', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=False, blank=True, default='')
    birthday = models.DateField(blank=True, verbose_name="Tug'ilgan kuni", null=True, default=datetime.date.today)
    username = models.CharField(max_length=30, unique=True, blank=True)
    phone = models.IntegerField('Tel raqam', null=True, blank=True, unique=True,
                                validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
    passport_seriya = models.CharField(max_length=10, null=True, blank=True)
    passport_number = models.IntegerField(null=True, blank=True)
    passport_photo = models.ImageField(upload_to=path_and_rename, null=True, blank=True)
    person_id = models.IntegerField('JShShIR',blank=True, null=True, )
    document_issue = models.DateField('Passport berilgan sana', blank=True, null=True)
    document_expiry = models.DateField('Passport amal qilish muddati', blank=True, null=True)
    issue_by_whom = models.CharField('Kim tomonidan berilgan', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    last_login = models.DateTimeField(null=True, auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    # gender = models.CharField('Jinsi', choices=GENDER_CHOICES, max_length=5, default='M')
    turbo = models.CharField(max_length=200, blank=True, null=True, validators=[MinLengthValidator(5)])

    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return f"{self.last_name} {self.first_name}"


class UserManager(BaseUserManager):

    def _create_user(self, email, username, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise Http404
        if not username:
            raise Http404
        now = timezone.now()
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            username=username,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            last_login=now,
            date_joined=now,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        return self._create_user(username, password, False, False, **extra_fields)

    def create_superuser(self, email, username, password, **extra_fields):
        user = self._create_user(email, username, password, True, True, **extra_fields)
        user.save(using=self._db)
        return user

def organization_rename(instance, filename):
    upload_to = 'organizations/certificate/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.identification_number:
        filename = '{}.{}'.format(instance.identification_number, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

def organization_rename2(instance, filename):
    upload_to = 'organizations/license/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.identification_number:
        filename = '{}.{}'.format(instance.identification_number, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)

class Organization(models.Model):
    title = models.CharField("Tashkilot nomi", max_length=255)
    certificate_photo = models.ImageField('Guvohnoma surati',upload_to=organization_rename,null=True)
    license_photo = models.ImageField('Litsenziya surati', upload_to=organization_rename2,null=True)
    identification_number = models.IntegerField('STIR',null=True,)
    legal_address = models.CharField("Yuridik manzili", max_length=255)
    address_of_garage = models.CharField("Garaj manzili", max_length=255)
    director = models.CharField(max_length=50, null=True)
    created_user = models.ForeignKey(User,verbose_name='Yaratgan shaxs', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(editable=False, verbose_name='Yaratgan vaqti', null=True)
    updated_date = models.DateTimeField(verbose_name='Tahrirlangan vaqti', null=True)
    removed_date = models.DateTimeField(editable=False, verbose_name='O\'chirilgan vaqti', null=True)
    is_active = models.BooleanField(verbose_name='Holati',default=True)

    class Meta:
        verbose_name = "Tashkilot"
        verbose_name_plural = "Tashkilotlar"

    def __str__(self):
        return f"{self.title}"


    def save(self, *args, **kwargs):
        ''' On save, update timestamps '''
        if not self.id:
            self.created_date = timezone.now()
        self.updated_date = timezone.now()
        return super().save(*args, **kwargs)


class Car(models.Model):
    model = models.CharField('Nomi', max_length=50)
    is_local = models.BooleanField('Mahalliy brend', default=False)
    is_truck = models.BooleanField('Yuk mashinasi', default=False)
    is_show = models.BooleanField(default=False)
    body_type = models.CharField('Kuzov turi', max_length=100, blank=True)
    body_number = models.CharField('Kuzov raqami', max_length=50, blank=True)
    chassis_number = models.CharField("Shassi raqami", max_length=255, blank=True)
    engine_number = models.CharField('Dvigitel raqami', max_length=50, blank=True)
    made_year = models.IntegerField("Ishlab chiqarilgan yili", null=True, blank=True)
    color = models.CharField('Rangi', max_length=50, blank=True)
    additionally = models.CharField('Qo\'shimcha jihozlar', max_length=100, null=True, blank=True)
    given_number = models.CharField('Berilgan davlat raqami', max_length=30, blank=True)
    given_technical_passport = models.CharField('Berilgan texpassport seriyasi', max_length=30, blank=True)



    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'

    def __str__(self):
        return self.model

