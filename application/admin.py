from django.contrib import admin

from application.models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'process','process_sms','service','file_name','person_type', 'created_user','created_date', 'updated_date', 'password']
    list_display_links = ['service',]
    save_on_top = True
    list_filter = [ 'process', 'person_type','created_date', ]


@admin.register(StateDutyTitle)
class StateDutyTitleAdmin(admin.ModelAdmin):
    list_display = ['id', 'title',]
    list_display_links = ['id',]
    save_on_top = True


@admin.register(StateDutyPercent)
class StateDutyPercentAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'state_duty', 'percent']
    list_display_links = ['id',]
    save_on_top = True
