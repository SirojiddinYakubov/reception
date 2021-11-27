import os
from time import time
from uuid import uuid4

from autoslug import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.utils.text import slugify as default_slugify, slugify

# Create your models here.
from django.utils.text import slugify

from user.models import User


class HelpSection(models.Model):
    title = models.CharField("Nomi (o'zbek tilida)", max_length=255, db_index=True)
    meta_desc = models.CharField("Mazmuni (rus tilida)", max_length=255, db_index=True, blank=True)
    meta_key = models.CharField("Kalit so'zlari (rus tilida)", max_length=255, db_index=True, blank=True)
    # slug = AutoSlugField()
    slug = AutoSlugField("URL (avtomatik qiladi)",populate_from=lambda instance: instance.title,
                         unique_with=['pub_date__month'],
                         slugify=lambda value: default_slugify(value.replace(' ','-').lower().replace(' ', '-').replace('а', 'a').replace('б', 'b').replace('в','v').replace('г', 'g').replace('д', 'd').replace('е', 'e').replace('ё', 'yo').replace( 'ж', 'zh').replace('з', 'z').replace('и', 'i').replace('й', 'j').replace('к', 'k').replace('л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р', 'r').replace('с', 's').replace('т', 't').replace('у', 'u').replace('ф', 'f').replace('х', 'kh').replace('ц', 'ts').replace( 'ч', 'ch').replace('ш', 'sh').replace('щ', 'shch').replace('ы', 'i').replace('э', 'e').replace('ю', 'yu').replace('я', 'ya').replace('ь', '').replace(',', '').replace('.', '').replace('.', '')), editable=True, blank=True)
    '''
 populate_from=lambda instance: instance.title,
                         unique_with=['pub_date__month'],
                         slugify=lambda value: default_slugify(value.replace(' ','-').lower().replace(' ', '-').replace('а', 'a').replace('б', 'b').replace('в','v').replace('г', 'g').replace('д', 'd').replace('е', 'e').replace('ё', 'yo').replace( 'ж', 'zh').replace('з', 'z').replace('и', 'i').replace('й', 'j').replace('к', 'k').replace('л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р', 'r').replace('с', 's').replace('т', 't').replace('у', 'u').replace('ф', 'f').replace('х', 'kh').replace('ц', 'ts').replace( 'ч', 'ch').replace('ш', 'sh').replace('щ', 'shch').replace('ы', 'i').replace('э', 'e').replace('ю', 'yu').replace('я', 'ya').replace('ь', '').replace(',', '').replace('.', '').replace('.', '')), editable=True, blank=True    '''

    pub_date = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField("Tartiblash", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class HelpArticle(models.Model):
    # section = models.ForeignKey(HelpSection, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_articles', verbose_name="Bo'lim")
    section = models.ForeignKey(HelpSection, on_delete=models.CASCADE, related_name='articles', verbose_name="Bo'lim")
    view = models.IntegerField(default=1, verbose_name="Ko'rilganlar")
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Nomi (rus tilida)", max_length=255, db_index=True)
    meta_desc = models.CharField("Mazmuni (o'zbek tilida)", max_length=255, db_index=True, blank=True)
    meta_key = models.CharField("Kalit so'zlari (o'zbek tilida)", max_length=255, db_index=True, blank=True)
    text = RichTextUploadingField("Maqola (rus tilida)", max_length=50000, db_index=True)
    updated_date = models.DateTimeField("Tahrirlangan vaqti", auto_now=True)
    author = models.ForeignKey(User, verbose_name="Muallif", on_delete=models.CASCADE)
    # slug = AutoSlugField()
    slug = AutoSlugField("Maqola URL (avtomatik qiladi)",populate_from=lambda instance: instance.title,
                         unique_with=['pub_date__month'],
                         slugify=lambda value: default_slugify(value.replace(' ','-').lower().replace(' ', '-').replace('а', 'a').replace('б', 'b').replace('в','v').replace('г', 'g').replace('д', 'd').replace('е', 'e').replace('ё', 'yo').replace( 'ж', 'zh').replace('з', 'z').replace('и', 'i').replace('й', 'j').replace('к', 'k').replace('л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р', 'r').replace('с', 's').replace('т', 't').replace('у', 'u').replace('ф', 'f').replace('х', 'kh').replace('ц', 'ts').replace( 'ч', 'ch').replace('ш', 'sh').replace('щ', 'shch').replace('ы', 'i').replace('э', 'e').replace('ю', 'yu').replace('я', 'ya').replace('ь', '').replace(',', '').replace('.', '').replace('.', '')), editable=True, blank=True )
    sort = models.IntegerField("Tartiblash", null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Maqola"
        verbose_name_plural = "Maqolalar"


class Helpful(models.Model):
    help_article = models.ForeignKey(HelpArticle, verbose_name="Maqola", on_delete=models.CASCADE)
    ip = models.GenericIPAddressField("Ip manzil", max_length=20)
    status = models.BooleanField("Holati", default=False)

    def __str__(self):
        return self.ip

    class Meta:
        verbose_name = "Baho"
        verbose_name_plural = "Baholar"
