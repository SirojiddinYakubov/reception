from django.contrib import admin

from click.models import Order


# @admin.register(Order)
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['id', 'user', 'is_paid', 'application', 'amount', 'created_at', 'updated_at']
#     list_display_links = ['user']
#     search_fields = ['user__first_name', 'user__last_name', 'user__middle_name', 'application__id']
#     list_filter = ['is_paid', 'created_at', 'updated_at', 'type']
#     save_on_top = True
