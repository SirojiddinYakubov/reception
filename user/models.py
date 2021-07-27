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
    is_active = models.BooleanField(default=True)

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
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', ]
        verbose_name = 'Tuman/Shahar'
        verbose_name_plural = 'Tumanlar/Shaharlar'


class Quarter(models.Model):
    title = models.CharField('Nomi', max_length=255)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True)
    sort = models.IntegerField(blank=True, default=1)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['sort', ]
        verbose_name = 'Mahalla'
        verbose_name_plural = 'Mahallalar'


class Section(models.Model):
    parent = models.ForeignKey('self', verbose_name=_("Bo'ysinuvchi tashkilot"), on_delete=models.CASCADE, null=True,
                               blank=True)
    title = models.CharField(max_length=300, verbose_name="Bo'lim nomi", blank=True, null=True)
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ManyToManyField(District, verbose_name='Tuman/Shahar', blank=True)
    is_active = models.BooleanField(default=True)
    pay_for_service = models.BooleanField(default=True)
    address = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"

    def __str__(self):
        return f"{self.title}: {self.region.title}"




# ROLE_CHOICES = (
#     ("1", "User"),  # Oddiy foydalanuvchilar
#     ("2", "Controller"),  # Xodimlar nazoratchisi
#     ("3", "Checker"),  # Arizalarni tekshiruvchi xodim
#     ("4", "Reviewer"),  # Ma'lumotlar mosligini tasdiqlovchi xodim
#     ("5", "Technical"),  # Texnik ko'rik o'tkazuvchi xodim
#
# )

USER = 1
CHECKER = 2
REVIEWER = 3
TECHNICAL = 4
DISTRICAL_CONTROLLER = 5
REGIONAL_CONTROLLER = 6
STATE_CONTROLLER = 7
MODERATOR = 8
ADMINISTRATOR = 9
SUPER_ADMINISTRATOR = 10

ROLE = (
    (USER, 'Oddiy foydalauvchi'),
    (CHECKER, 'Arizalarni tekshiruvchi xodim'),
    (REVIEWER, 'Ma\'lumotlar mosligini tasdiqlovchi xodim'),
    (TECHNICAL, 'Texnik ko\'rik o\'tkazuvchi xodim'),
    (DISTRICAL_CONTROLLER, 'Tuman nazoratchisi'),
    (REGIONAL_CONTROLLER, 'Viloyat nazoratchisi'),
    (STATE_CONTROLLER, 'Davlat nazoratchisi'),
    (MODERATOR, 'Moderator'),
    (ADMINISTRATOR, 'Administrator'),
    (SUPER_ADMINISTRATOR, 'Super administrator')
)

MAN = 0
WOMAN = 1

GENDER_CHOICES = (
    (MAN, _('Erkak')),
    (WOMAN, _('Ayol')),
)

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
    last_name = models.CharField(verbose_name='Familiya', max_length=255, blank=True)
    first_name = models.CharField(verbose_name='Ism', max_length=255, blank=True)
    middle_name = models.CharField(verbose_name='Otasining ismi', max_length=255, blank=True)
    role = models.IntegerField(verbose_name='Foydalanuvchi roli', choices=ROLE,  default=USER)
    region = models.ForeignKey(Region, verbose_name='Viloyat', on_delete=models.SET_NULL, null=True, blank=True)
    district = models.ForeignKey(District, verbose_name='Tuman/Shahar', on_delete=models.SET_NULL, null=True,
                                 blank=True)
    section = models.ForeignKey(Section, verbose_name="Bo'lim", on_delete=models.SET_NULL, null=True, blank=True)
    quarter = models.ForeignKey(Quarter, on_delete=models.SET_NULL, verbose_name='Mahalla', null=True, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    email = models.EmailField(max_length=254, unique=False, blank=True, default='')
    birthday = models.DateField(blank=True, verbose_name="Tug'ilgan kuni", null=True, default=timezone.now)
    username = models.CharField(max_length=30, unique=True, blank=True)
    phone = models.IntegerField('Tel raqam', null=True, blank=True, unique=True,
                                validators=[MaxValueValidator(999999999), MinValueValidator(100000000)])
    passport_seriya = models.CharField(max_length=10, null=True, blank=True)
    passport_number = models.IntegerField(null=True, blank=True)
    person_id = models.BigIntegerField('JShShIR', blank=True, null=True, )
    issue_by_whom = models.CharField('Kim tomonidan berilgan', max_length=30, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False, blank=True)
    is_active = models.BooleanField(default=True, blank=True)
    last_login = models.DateTimeField(null=True, auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    gender = models.IntegerField(verbose_name='Jinsi', choices=GENDER_CHOICES, default=MAN)
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
    # certificate_photo = models.ImageField('Guvohnoma surati',upload_to=organization_rename,null=True)
    # license_photo = models.ImageField('Litsenziya surati', upload_to=organization_rename2,null=True)
    identification_number = models.IntegerField('STIR', null=True, )
    legal_address_region = models.ForeignKey(Region, on_delete=models.SET_NULL, verbose_name="Yuridik manzil(Viloyat)",
                                             null=True)
    legal_address_district = models.ForeignKey(District, on_delete=models.SET_NULL,
                                               verbose_name="Yuridik manzil(Tuman)", null=True)
    address_of_garage = models.CharField("Garaj manzili", max_length=255)
    director = models.CharField(max_length=50, verbose_name='Rahbari', null=True)
    created_user = models.ForeignKey(User, verbose_name='Yaratgan shaxs', on_delete=models.CASCADE, null=True)
    created_date = models.DateTimeField(editable=False, verbose_name='Yaratgan vaqti', null=True)
    updated_date = models.DateTimeField(verbose_name='Tahrirlangan vaqti', null=True)
    removed_date = models.DateTimeField(editable=False, verbose_name='O\'chirilgan vaqti', null=True)
    is_active = models.BooleanField(verbose_name='Holati', default=True)

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


class CarModel(models.Model):
    title = models.CharField('Nomi', max_length=50)
    creator = models.CharField('Ishlab chiqaruvchi', null=True, blank=True, max_length=100)
    is_local = models.BooleanField('Mahalliy brend', default=False)
    is_truck = models.BooleanField('Yuk mashinasi', default=False)
    is_active = models.BooleanField(default=True)
    created_user = models.ForeignKey(User, verbose_name='Yaratgan shaxs', on_delete=models.SET_NULL, null=True)
    created_date = models.DateTimeField(verbose_name="Yaratilgan vaqti", default=timezone.now)

    class Meta:
        verbose_name = 'Avtomobil rusumi'
        verbose_name_plural = 'Avtomobillar rusumi'

    def __str__(self):
        return str(self.title)


class Car(models.Model):
    model = models.ForeignKey(CarModel, verbose_name="Model", on_delete=models.SET_NULL, null=True, related_name='car_model')
    body_type = models.ForeignKey('BodyType', verbose_name='Kuzov turi', on_delete=models.SET_NULL, blank=True,
                                  null=True)
    fuel_type = models.ManyToManyField('FuelType', verbose_name='Yoqilg\'i turi', blank=True,
                                       related_name='car_fuel_type')
    re_fuel_type = models.ManyToManyField('FuelType', verbose_name='Qo\'shimcha o\'rnatilgan yoqilg\'i turi',
                                          blank=True, related_name='car_re_fuel_type')
    full_weight = models.IntegerField(verbose_name='To\'la vazni', null=True, blank=True, default=0)
    empty_weight = models.IntegerField(verbose_name='Yuksiz vazni', null=True, blank=True, default=0)
    type = models.ForeignKey('CarType', on_delete=models.SET_NULL, verbose_name='Avtomobil turi', blank=True, null=True)
    device = models.ManyToManyField('Device', verbose_name='Alohida belgilar', blank=True)
    body_number = models.CharField(verbose_name='Kuzov raqami', max_length=50, blank=True)
    chassis_number = models.CharField(verbose_name="Shassi raqami", max_length=255, blank=True, null=True)
    engine_number = models.CharField(verbose_name='Dvigitel raqami', max_length=50, blank=True)
    made_year = models.DateField(verbose_name="Ishlab chiqarilgan yili", null=True, blank=True)
    color = models.ForeignKey('Color', verbose_name='Rangi', on_delete=models.SET_NULL, null=True, blank=True,
                              related_name='car_color')
    re_color = models.ForeignKey('Color', verbose_name='Qayta ranglangan', on_delete=models.SET_NULL, null=True,
                                 blank=True, related_name='car_re_color')
    engine_power = models.IntegerField(verbose_name='Dvigatel quvvati', null=True, blank=True, default=0)
    old_number = models.CharField(verbose_name='Eski DRB', null=True, blank=True, max_length=15)
    old_technical_passport = models.CharField(verbose_name='Eski texpassport seriyasi va raqami', max_length=30, blank=True)
    is_old_number = models.BooleanField(verbose_name='Avtompobildagi DRB eski', default=False)
    given_technical_passport = models.CharField(verbose_name='Berilgan texpassport seriyasi va raqami', max_length=30, blank=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False, verbose_name='Yaratilgan vaqti')
    lost_technical_passport = models.BooleanField(verbose_name='Texnik passport yo\'qolgan', default=False)
    lost_number = models.BooleanField(verbose_name='DRB yo\'qolgan', default=False)
    is_confirm = models.BooleanField(verbose_name='Ma\'lumotlar mosligi', default=False)
    confirm_date = models.DateTimeField(null=True, blank=True)
    is_technical_confirm = models.BooleanField(verbose_name='Texnik ko\'rik', default=False)
    technical_confirm_date = models.DateTimeField(null=True, blank=True)
    is_new = models.BooleanField(verbose_name='Avtomobil yangi', default=False)
    price = models.BigIntegerField(verbose_name='Avtomobil narxi', default=0, blank=True)
    history = models.ForeignKey('Car', verbose_name='Avtomobil tarixi', on_delete=models.SET_NULL, blank=True,
                                null=True)
    is_auction = models.BooleanField(default=False, verbose_name='Raqam auksiondan olingan')
    given_number = models.CharField(verbose_name='Yangi DRB', max_length=15, blank=True, null=True)

    is_replace_number = models.BooleanField(verbose_name='Yangi raqam olish', default=False)
    is_road_fund = models.BooleanField(verbose_name="Yo'l fondi uchun to'lov", default=False)

    class Meta:
        verbose_name = 'Avtomobil'
        verbose_name_plural = 'Avtomobillar'

    def __str__(self):
        return str(self.model)


class CarType(models.Model):
    title = models.CharField('Nomi', max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Transport vositasi turi'
        verbose_name_plural = 'Transport vositasi turlari'

    def __str__(self):
        return str(self.title)


class BodyType(models.Model):
    title = models.CharField('Nomi', max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Kuzov turi'
        verbose_name_plural = 'Kuzov turlari'

    def __str__(self):
        return str(self.title)


class Device(models.Model):
    title = models.CharField('Nomi', max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Qo\'shimcha qurilma'
        verbose_name_plural = 'Qo\'shimcha qurilmalar'

    def __str__(self):
        return str(self.title)


class FuelType(models.Model):
    title = models.CharField('Nomi', max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)

    class Meta:
        verbose_name = 'Yoqilg\'i turi'
        verbose_name_plural = 'Yoqilg\'i turlari'

    def __str__(self):
        return str(self.title)


class Color(models.Model):
    title = models.CharField('Nomi', max_length=100)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(default=timezone.now, editable=False)
    created_user = models.ForeignKey(User, verbose_name='Yaratgan shaxs', on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name = 'Rang'
        verbose_name_plural = 'Ranglar'

    def __str__(self):
        return str(self.title)


class Constant(models.Model):
    key = models.CharField('Nomi', max_length=150, editable=False)
    value = models.CharField('Qiymati', max_length=150)
    info = models.CharField('Ma\'lumot', max_length=250)

    class Meta:
        verbose_name = 'Constant'
        verbose_name_plural = 'Constantlar'

    def __str__(self):
        return f"{self.key}: {self.value}"
