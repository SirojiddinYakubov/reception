from django.contrib import admin
from .models import *
# Register your models here.

# admin.site.register(AccountStatementDocument)



@admin.register(AccountStatement)
class AccountStatementAdmin(admin.ModelAdmin):
    list_display = ['id', 'make_cert', 'date_conclusion_contract','person_type']
    list_display_links = ['make_cert']
    list_filter = ['person_type' ]

    def make_cert(self,obj):
        cert =  f'{obj.cert_seriya} №{obj.cert_number}'
        return cert

    make_cert.allow_tags = True
    make_cert.short_description = "Guvohnoma"

