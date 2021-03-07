from django.contrib import admin

# Register your models here.
from gift_agreement.models import GiftAgreement


@admin.register(GiftAgreement)
class GiftAgreementAdmin(admin.ModelAdmin):
    list_display = ['id', 'seriya','car','organization', 'created_user','date_conclusion_contract','person_type', ]
    list_display_links = ['seriya']
    list_filter = ['person_type' , 'created_date', 'date_conclusion_contract']