from django.contrib import admin
from django.forms import *

from service.models import *


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    # def render_change_form(self, request, context, *args, **kwargs):
    #     context['adminform'].form.fields['document'].queryset = Document.objects.filter(is_active=False)
    #
    #     return super().render_change_form(request, context, *args, **kwargs)

    list_display = ['id', 'short_title', 'key', ]
    list_display_links = ['short_title']
    list_filter = ['created_date', ]
    search_fields = ['short_title', 'key']


# @admin.register(Document)
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ['id','title',  ]
#     list_display_links = ['id','title']
#     list_filter = [ 'created_date',]
#     search_fields = ['title', ]

@admin.register(StateDuty)
class StateDutyAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'size': '300'})},
    # }

    list_display = ['id', 'application', 'score', 'percent']
    search_fields = ['application', 'score']
    list_filter = ['application']
    list_display_links = ['id', 'application']
    save_on_top = True


@admin.register(StateDutyPercent)
class StateDutyPercentAdmin(admin.ModelAdmin):
    list_display = ['id', 'state_duty', 'car_type', 'person_type', 'percent', 'car_is_new', 'is_old_number',
                    'lost_number', 'lost_technical_passport', 'start', 'stop']
    list_display_links = ['id', 'state_duty']
    list_filter = ['state_duty', 'car_type', 'person_type', 'is_old_number', 'lost_number', 'lost_technical_passport', ]
    save_on_top = True


@admin.register(StateDutyScore)
class StateDutyScoreAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'size': '300'})},
    # }

    list_display = ['id', 'state_duty', 'region', 'district', 'score', 'created_date', 'updated_date']
    search_fields = ['district__title', 'region__title', 'score']
    list_filter = ['created_date', 'region', 'state_duty']
    list_display_links = ['id', 'state_duty']
    save_on_top = True


@admin.register(ExampleDocument)
class ExampleDocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['title']
    list_filter = ['created_at', 'updated_at']
    search_fields = ['title', ]


@admin.register(AmountBaseCalculation)
class AmountBaseCalculationAdmin(admin.ModelAdmin):
    list_display = ['id', 'amount', ]
    list_display_links = ['amount']
    list_filter = ['start', 'stop']
    search_fields = ['amount', ]
