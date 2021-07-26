from django.contrib import admin

from application.models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'process','process_sms','service','file_name','person_type', 'created_user','created_date', 'updated_date', 'password']
    list_display_links = ['process',]
    save_on_top = True
    list_filter = [ 'process', 'person_type','created_date', ]



