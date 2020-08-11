from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(AccountStatementDocument)



@admin.register(AccountStatement)
class AccountStatementAdmin(admin.ModelAdmin):
    list_display = ['id','is_checked','is_deleted','technical_inspection',  'car', 'user', 'make_cert', 'date_conclusion_contract','engine_number', 'body_number', 'color', 'chassis_number','made_year','person_type', 'organization','pub_date']
    list_display_links = ['car','user','make_cert']
    list_filter = ['is_checked', 'is_deleted', 'technical_inspection', 'person_type','pub_date', ]

    def make_cert(self,obj):
        cert =  f'{obj.cert_seriya} №{obj.cert_number}'
        return cert

    make_cert.allow_tags = True
    make_cert.short_description = "Guvohnoma"

