from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from user.models import User

# Create your models here.


class HelpSection(models.Model):
    title = models.CharField(max_length=255, db_index=True)
    meta_desc = models.CharField(max_length=255, db_index=True, blank=True)
    meta_key = models.CharField(max_length=255, db_index=True, blank=True)
    slug = models.SlugField(unique=True)
    pub_date = models.DateTimeField(auto_now_add=True)
    sort = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Bo'lim"
        verbose_name_plural = "Bo'limlar"


class HelpArticle(models.Model):
    # section = models.ForeignKey(HelpSection, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_articles', verbose_name="Bo'lim")
    section = models.ForeignKey(HelpSection, on_delete=models.CASCADE, related_name='articles')
    view = models.IntegerField(default=1)
    pub_date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255, db_index=True)
    meta_desc = models.CharField(max_length=255, db_index=True, blank=True)
    meta_key = models.CharField(max_length=255, db_index=True, blank=True)
    text = RichTextUploadingField(max_length=1000000, db_index=True)
    updated_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    sort = models.IntegerField(null=True, blank=True)

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


'''
populate_from=lambda instance: instance.title,
                       unique_with=['pub_date__month'],
                       slugify=lambda value: default_slugify(value.replace(' ','-').lower().replace(' ', '-').replace('а', 'a').replace('б', 'b').replace('в','v').replace('г', 'g').replace('д', 'd').replace('е', 'e').replace('ё', 'yo').replace( 'ж', 'zh').replace('з', 'z').replace('и', 'i').replace('й', 'j').replace('к', 'k').replace('л', 'l').replace('м', 'm').replace('н', 'n').replace('о', 'o').replace('п', 'p').replace('р', 'r').replace('с', 's').replace('т', 't').replace('у', 'u').replace('ф', 'f').replace('х', 'kh').replace('ц', 'ts').replace( 'ч', 'ch').replace('ш', 'sh').replace('щ', 'shch').replace('ы', 'i').replace('э', 'e').replace('ю', 'yu').replace('я', 'ya').replace('ь', '').replace(',', '').replace('.', '').replace('.', '')), editable=True, blank=True    '''
