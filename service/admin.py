from django.contrib import admin

from service.models import *

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'seriya', 'car','organization','created_user','contract_date','person_type', ]
    list_display_links = ['seriya']
    list_filter = ['person_type' , 'created_date', 'contract_date']
    search_fields = ['title', 'seriya']


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
