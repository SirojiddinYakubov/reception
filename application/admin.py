from django.contrib import admin

from application.models import *


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'process', 'service', 'file_name', 'person_type', 'created_user',
                    'created_date', 'updated_date', 'password']
    list_display_links = ['process', ]
    save_on_top = True
    list_filter = ['process', 'person_type', 'created_date', 'is_active']


# @admin.register(ApplicationDocument)
# class ApplicationDocumentAdmin(admin.ModelAdmin):
#     list_display = ['id', 'application', 'example_document', 'seriya', 'contract_date', 'created_at', 'updated_at']
#     list_display_links = ['application', 'example_document']
#     list_filter = ['application__service__short_title', ]
#     save_on_top = True


@admin.register(ApplicationDocumentAttachment)
class ApplicationDocumentAttachmentAdmin(admin.ModelAdmin):
    list_display = ['id', 'application_document', 'attachment', 'created_at', 'updated_at']
    list_display_links = ['application_document', ]
    list_filter = ['application_document__application__service__short_title', ]
    save_on_top = True


@admin.register(ApplicationCashByModerator)
class ApplicationCashByModeratorAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'application', 'moderator', 'created_at']
    list_display_links = ['id', 'status', 'application', ]
    # search_fields = ['application']
    list_filter = ['status', 'created_at', 'application__service__short_title', 'application__process',
                   'moderator__role', 'moderator__region']
    save_on_top = True

admin.site.register(ApplicationDocument)