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
    list_display_links = ['id','short_title']
    list_filter = ['created_date', ]
    search_fields = ['short_title', 'key']


# @admin.register(Document)
# class DocumentAdmin(admin.ModelAdmin):
#     list_display = ['id','title',  ]
#     list_display_links = ['id','title']
#     list_filter = [ 'created_date',]
#     search_fields = ['title', ]

@admin.register(PaidStateDuty)
class PaidStateDutyAdmin(admin.ModelAdmin):
    # formfield_overrides = {
    #     models.IntegerField: {'widget': NumberInput(attrs={'size': '300'})},
    # }

    list_display = ['id', 'application', 'score', 'percent']
    search_fields = ['application', 'score']
    list_filter = ['score__state_duty', 'created_date', 'is_return', 'application__created_user__region']
    list_display_links = ['id', 'application']
    save_on_top = True


@admin.register(StateDutyPercent)
class StateDutyPercentAdmin(admin.ModelAdmin):
    def get_car_types(self, obj):
        return ", ".join([i.title for i in obj.car_type.all()])

    def services(self, obj):
        return ", ".join([i.short_title for i in obj.service.all()])

    list_display = ['id', 'title', 'state_duty', 'services', 'get_car_types', 'person_type', 'percent',
                    'is_save_old_number', 'is_tranzit', 'is_relative', 'is_saved_number', 'is_auction', 'car_is_new',
                    'is_old_number',
                    'lost_number', 'lost_technical_passport', 'start', 'stop']
    list_display_links = ['id', 'state_duty']
    search_fields = ['title']
    list_filter = ['state_duty', 'person_type', 'is_old_number', 'lost_number', 'lost_technical_passport', ]
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


@admin.register(GetPayFromCard)
class GetPayFromCardAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_id', 'application', 'card_number', 'amount']
    list_display_links = ['transaction_id']
    list_filter = ['created_at', ]
    search_fields = ['transaction_id', 'application_id', 'card_number', ]


@admin.register(PaymentForTreasury)
class PaymentForTreasuryAdmin(admin.ModelAdmin):
    list_display = ['id', 'transaction_id', 'application',  'state_duty_score',
                    'state_duty_percent']
    list_display_links = ['application']
    list_filter = ['created_at', ]
    search_fields = ['transaction_id', 'application_id',]
