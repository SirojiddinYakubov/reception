from django.contrib import admin
from django.utils.safestring import mark_safe

from user.models import *


@admin.register(User)
class UserAdmin(admin.ModelAdmin):

    list_display = ['id', 'role', 'last_name', 'first_name','middle_name', 'phone','fullpassport', 'turbo', 'birthday', 'is_active',
                    'is_superuser', 'is_staff', 'date_joined','last_login']
    list_display_links = [ 'role', 'last_name', 'first_name','middle_name',]
    list_filter = ['role','is_active', ]
    search_fields = ['last_name', 'first_name','middle_name', 'username', 'phone', 'passport_seriya', 'passport_number','turbo',]
    save_on_top = True

    # def get_img(self, obj):
    #     if obj.passport_photo:
    #         return mark_safe(f"<img src='{obj.passport_photo.url}' alt='passport_photo' width=50px>")
    #     else:
    #         pass

    def fullpassport(self, obj):
        if obj.passport_seriya:
            return f'{obj.passport_seriya}{obj.passport_number}'
        else:
            return '-'

    def save_model(self, request, obj, form, change):
        obj.set_password(obj.turbo)
        obj.username = obj.phone
        obj.save()
        return super().save_model(request, obj, form, change)


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

class QuarterInline(admin.StackedInline):
    model = Quarter
    extra = 5


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['title']}),
    ]
    inlines = [QuarterInline]
    save_on_top = True


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'parent','title','region','get_districts']
    list_display_links = ['title',]
    save_on_top = True

    def get_districts(self, obj):
        return ",\n".join([p.title for p in obj.district.all()])

@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
    list_display_links = ['title']
    save_on_top = True

# @admin.register(UserPassword)
# class UserPasswordAdmin(admin.ModelAdmin):
#     list_display = ['id', 'phone', 'password']
#     list_display_links = ['phone',]
#     save_on_top = True

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ['id', 'model','created_date' ]
    list_display_links = ['model']
    save_on_top = True

@admin.register(CarModel)
class CarModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['title']
    save_on_top = True

@admin.register(FuelType)
class FuelTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['title']
    save_on_top = True

@admin.register(CarType)
class CarTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    list_display_links = ['title']
    save_on_top = True

@admin.register(BodyType)
class BodyTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','created_date' ]
    list_display_links = ['title']
    save_on_top = True

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','created_date' ]
    list_display_links = ['title']
    save_on_top = True


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'title','created_date' ]
    list_display_links = ['title']
    save_on_top = True


from rest_framework.authtoken.admin import TokenAdmin
# TokenAdmin.raw_id_fields = ['user']

@admin.register(Constant)
class ConstantAdmin(admin.ModelAdmin):
    list_display = ['id', 'info','value' , ]
    list_display_links = [ 'value', 'info']
    search_fields = ['key', 'value']
    readonly_fields = ('info',)
    save_on_top = True