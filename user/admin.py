from django.contrib import admin
from user.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'role', 'last_name', 'first_name','middle_name', 'phone', 'turbo', 'birthday', 'is_active',
                    'is_superuser', 'is_staff', 'date_joined',
                    'last_login']
    list_display_links = [ 'role', 'last_name', 'first_name','middle_name',]
    list_filter = ['role','is_active', ]
    search_fields = ['last_name', 'first_name','middle_name', 'username', 'phone', 'passport','turbo',]
    save_on_top = True

class DistrictInline(admin.StackedInline):
    model = District
    extra = 5


@admin.register(Region)
class RegionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [DistrictInline]
    save_on_top = True

class MFYInline(admin.StackedInline):
    model = MFY
    extra = 5


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [MFYInline]
    save_on_top = True


@admin.register(Nationality)
class NationalityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sort']
    list_display_links = ['title']
    save_on_top = True


