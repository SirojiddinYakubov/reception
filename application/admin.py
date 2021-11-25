from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from application.models import *

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['id', 'process', 'service', 'link_to_application_document', 'person_type', 'created_user',
                    'created_date', 'updated_date', 'password']
    list_display_links = ['process', ]
    search_fields = ['created_user__last_name', 'created_user__first_name', 'created_user__middle_name', 'id']
    save_on_top = True
    list_filter = ['service', 'process', 'person_type', 'created_date', 'is_active', 'section']

    def link_to_application_document(self, obj):
        if hasattr(obj, 'applicationdocument_set'):
            application_document = obj.applicationdocument_set.all().last()
            if application_document:
                url = reverse('admin:%s_%s_change' % (
                application_document._meta.app_label, application_document._meta.model_name),
                              args=[application_document.id])
                return mark_safe(f'<a href="{url}">{application_document.seriya}</a>')
    link_to_application_document.short_description = 'document'
    link_to_application_document.allow_tags = True


@admin.register(ApplicationDocument)
class ApplicationDocumentAdmin(admin.ModelAdmin):
    list_display = ['id', 'application', 'example_document', 'seriya', 'contract_date', 'created_at', 'updated_at']
    list_display_links = ['application', 'example_document']
    list_filter = ['application__service__short_title', ]
    save_on_top = True


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


@admin.register(DocumentForPolice)
class DocumentForPoliceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'get_services', 'is_active']
    list_display_links = ['title', 'get_services', ]
    save_on_top = True
    list_filter = ['title', 'created_at', 'is_active']

    def get_services(self, obj):
        return ",\n".join([p.short_title for p in obj.service.all()])
