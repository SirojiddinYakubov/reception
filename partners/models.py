from django.db import models
from user.models import *

""" Notariuslar bo'limi """

# Create your models here.
class NotaryDepartment(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Viloyat")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="Tuman")
    address = models.CharField(verbose_name="Manzil", max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    title = models.CharField(verbose_name="Notarius nomi", max_length=255)
    phone = models.IntegerField(verbose_name="Telefon raqami")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Notarius"
        verbose_name_plural = "Notariuslar"

    # Notariusning bo'sh vaqtlari
class NotaryFreeTime(models.Model):
    notary_department = models.ForeignKey(NotaryDepartment, verbose_name="Notarius", on_delete=models.CASCADE)
    free_time = models.DateTimeField(verbose_name="Bo'sh vaqti")
    
    def __str__(self) -> str:
        return str(self.notary_department.title)

    class Meta:
        verbose_name = "Notarius bo'sh vaqti"
        verbose_name_plural = "Notarius bo'sh vaqtlari"


    # Notariusning bo'sh vaqtlariga yozilish
class BookingNotaryTime(models.Model):
    pass






""" Diagnostikalar bo'limi """
class DiagnosticDepartment(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Viloyat")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="Tuman")
    address = models.CharField(verbose_name="Manzil", max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    title = models.CharField(verbose_name="Notarius nomi", max_length=255)
    phone = models.IntegerField(verbose_name="Telefon raqami")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Diagnostika"
        verbose_name_plural = "Diagnostikalar"


""" Avtosalonlar bo'limi  """
class AutoSalon(models.Model):
    region = models.ForeignKey(Region, on_delete=models.CASCADE, verbose_name="Viloyat")
    district = models.ForeignKey(District, on_delete=models.CASCADE, verbose_name="Tuman")
    address = models.CharField(verbose_name="Manzil", max_length=255)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Longitude")
    latitude = models.DecimalField(max_digits=9, decimal_places=6, verbose_name="Latitude")
    title = models.CharField(verbose_name="Notarius nomi", max_length=255)
    phone = models.IntegerField(verbose_name="Telefon raqami")

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "Avtosalon"
        verbose_name_plural = "Avtosalonlar"