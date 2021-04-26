from django.contrib import admin
from django.forms import *

from service.models import *

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['id','title', 'seriya', 'car','organization','contract_date','person_type', ]
    list_display_links = ['seriya']
    list_filter = ['person_type' , 'created_date', 'contract_date']
    search_fields = ['title', 'seriya']

@admin.register(StateDuty)
class StateDutyAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'size': '300'})},
    # }

    list_display = ['id', 'title','payment', 'created_user',  'created_date', 'updated_date']
    search_fields = ['title', 'payment']
    list_filter = ['title']
    list_display_links = ['id','title']
    save_on_top = True

@admin.register(StateDutyPercent)
class StateDutyPercentAdmin(admin.ModelAdmin):
    list_display = ['id', 'state_duty','car_type','person_type', 'percent','car_is_new','is_old_number','lost_number','lost_technical_passport','start','stop' ]
    list_display_links = ['id','state_duty']
    list_filter = ['state_duty','car_type','person_type','is_old_number','lost_number','lost_technical_passport', ]
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