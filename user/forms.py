from django import forms

from user.models import *


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'phone', 'region', 'district', 'mfy', 'address',
                  'nationality', 'gender', 'passport', 'document_issue', 'document_expiry']
        exclude = ['password', 'email']
