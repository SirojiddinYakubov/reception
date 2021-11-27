from django import forms

from help.models import Helpful


class HelpfulForm(forms.ModelForm):
    class Meta:
        model = Helpful

        fields = ['status', 'help_article', 'ip']
