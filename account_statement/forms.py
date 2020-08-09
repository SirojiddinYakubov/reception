from django import forms

from .models import *


class AccountStatementForm(forms.ModelForm):
    class Meta:
        model = AccountStatement
        fields = ['person_type', 'car', 'user', 'cert_seriya', 'cert_number', 'date_conclusion_contract',
                  'engine_number', 'body_number',
                  'color', 'chassis_number']
        exclude = ['is_checked', 'is_deleted', 'technical_inspection', 'organization']
