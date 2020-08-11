from django import forms

from user.models import *


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name','birthday', 'phone', 'region', 'district', 'mfy', 'address',
                  'nationality', 'gender', 'document_issue', 'document_expiry', 'issue_by_whom']
        exclude = ['password', 'email', 'passport_seriya', 'passport_number']
