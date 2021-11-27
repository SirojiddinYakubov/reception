from django.contrib import admin

# Register your models here.
from help.models import *


@admin.register(HelpSection)
class HelpSectionAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['title']


@admin.register(HelpArticle)
class HelpArticleAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['title']


@admin.register(Helpful)
class HelpfulAdmin(admin.ModelAdmin):
    save_on_top = True
    search_fields = ['ip']
    list_display = ['ip', 'status']
    # readonly_fields = ['ip', 'status','help_article']



