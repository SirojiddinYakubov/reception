from django import forms

from .models import *


class AccountStatementForm(forms.ModelForm):
    class Meta:
        model = AccountStatement
        fields = ['person_type', 'cert_seriya', 'cert_number', 'date_conclusion_contract']
        exclude = []
