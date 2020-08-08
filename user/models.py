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



class Region(models.Model):
    title = models.CharField('Nomi', max_length=255)
    sort = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort',]
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


class Nationality(models.Model):
    title = models.CharField('Nomi', max_length=255)
    sort = models.IntegerField(blank=True, default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', ]
        verbose_name = 'Millat'
        verbose_name_plural = 'Millatlar'




ROLE_CHOICES = (
    ("1", "User"),
    ("2", "R.I.B"),
    ("3", "M.I.R.B"),

)

GENDER_CHOICES = (
    ('M', 'Erkak'),
    ('W', 'Ayol'),
)

class User(AbstractBaseUser, PermissionsMixin):
    last_name = models.CharField('Familiya',max_length=255)
    first_name = models.CharField('Ism',max_length=255)
    middle_name = models.CharField('Otasining ismi',max_length=255)
    role = models.CharField('Foydalanuvchi roli',choices=ROLE_CHOICES, max_length=15, default="1")
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    mfy = models.ForeignKey(MFY, on_delete=models.SET_NULL, verbose_name='MFY', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=False, blank=True, default='')

    birthday = models.DateField(blank=True, verbose_name="Tug'ilgan kuni", null=True, default=datetime.date.today)
    username = models.CharField(max_length=30, unique=True, blank=True)
    phone = models.IntegerField('Tel raqam',null=True, blank=True, unique=True, validators=[MaxValueValidator(999999999),MinValueValidator(100000000)])
    passport = models.CharField(max_length=20, null=True, unique=True)
    document_issue = models.DateField('Passport berilgan sana',blank=True, null=True)
    document_expiry = models.DateField('Passport amal qilish muddati',blank=True, null=True)
    nationality = models.ForeignKey(Nationality, verbose_name='Millati',on_delete=models.SET_NULL,null=True, blank=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    last_login = models.DateTimeField(null=True, auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.CharField('Jinsi',choices=GENDER_CHOICES, max_length=5,default='M')
    turbo = models.CharField(max_length=200, blank=True, null=True, validators=[MinLengthValidator(7)])

    USERNAME_FIELD = 'username'


    objects = UserManager()

    def __str__(self):
        return f"{self.first_name}"



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



