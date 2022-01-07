from django.contrib import admin

from driver_license.models import (CallToExam)


@admin.register(CallToExam)
class CallToExamAdmin(admin.ModelAdmin):
    list_display = ['id', 'pupil', 'phone', 'coming_date', 'is_send', 'created_at', 'is_active']
    list_display_links = ['id', 'pupil', 'phone', ]
    search_fields = ['title', 'phone']
    list_filter = ['is_send', 'created_at', 'is_active']
    save_on_top = True
