from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Car)
admin.site.register(AccountStatement)
admin.site.register(AccountStatementDocument)