from django.contrib import admin

from application.models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'process','process_sms','service','file_name','person_type', 'created_user','created_date', 'updated_date', 'password']
    list_display_links = ['service',]
    save_on_top = True
    list_filter = [ 'process', 'person_type','created_date', ]


# @admin.register(Service)
# class ServiceAdmin(admin.ModelAdmin):
#     list_display = ['id', 'account_statement', 'gift_agreement','contract_of_sale',]
#     list_display_links = ['id',]
#     save_on_top = True
