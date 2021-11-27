from django.contrib import admin
from partners import models


@admin.register(models.DiagnosticDepartment)
class DiagnosticDepartmentAdmin(admin.ModelAdmin):
    list_display = ['id',
                    'region',
                    'district',
                    'address',
                    'longitude',
                    'latitude',
                    'title',
                    'phone',
                    'created_at',
                    'updated_at'
                    ]

    list_display_links = ['region', 'district']
    list_filter = ['district', ]
    save_on_top = True
