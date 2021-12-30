from django.contrib import admin

from landing.models import (Vacancy)


@admin.register(Vacancy)
class VacancyAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'form', 'created_at', 'is_active']
    list_display_links = ['id', 'title', 'desc', ]
    search_fields = ['title']
    list_filter = [ 'created_at', 'is_active']
    save_on_top = True
