from django.contrib import admin

from application.models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'account_statement', 'is_checked', 'created_user','created_date', 'updated_date']
    list_display_links = ['id','account_statement']
    save_on_top = True
    list_filter = ['account_statement', 'is_checked', 'is_legal']
