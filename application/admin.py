from django.contrib import admin

from application.models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'process', 'process_sms', 'service', 'file_name', 'person_type', 'created_user',
                    'created_date', 'updated_date', 'password']
    list_display_links = ['process', ]
    save_on_top = True
    list_filter = ['process', 'person_type', 'created_date', 'is_active']


@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'application', 'example_ducument', 'seriya', 'contract_date', 'created_at', 'updated_at']
    list_display_links = ['application', 'example_ducument']
    list_filter = ['application__service__short_title', ]
    save_on_top = True


@admin.register(ApplicationDocumentAttachment)
class ApplicationDocumentAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'application_document', 'attachment', 'created_at', 'updated_at']
    list_display_links = ['application_document', ]
    list_filter = ['application_document__application__service__short_title', ]
    save_on_top = True
