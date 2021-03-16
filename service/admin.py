from django.contrib import admin
from django.forms import *

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
    list_display_links = ['id','service','state_duty']
    save_on_top = True


@admin.register(StateDutyScore)
class StateDutyScoreAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'size': '300'})},
    # }

    list_display = ['id', 'state_duty','region', 'district', 'score', 'created_date', 'updated_date']
    search_fields = ['district__title','region__title', 'score']
    list_filter = ['created_date', 'region', 'state_duty']
    list_display_links = ['id','state_duty']
    save_on_top = True