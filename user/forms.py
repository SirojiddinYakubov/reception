from django import forms
from django.forms import ModelForm

from user.models import *
from django.utils.translation import gettext as _


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name', 'birthday', 'person_id', 'phone', 'region', 'district',
                  'quarter', 'address',
                  'issue_by_whom']
        exclude = ['password', 'email', 'passport_seriya', 'passport_number']


class EditForm(forms.ModelForm):
    first_name = forms.CharField(label='Ism:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Masalan: Yoqubov', 'id': 'first_name'}))
    last_name = forms.CharField(label='Familiya:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Masalan: Sirojiddin', 'id': 'last_name'}))
    middle_name = forms.CharField(label='Otasining ismi:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Masalan: Tojiddinovich', 'id': 'middle_name'}))
    birthday = forms.DateField(label="Tug'ilgan  kuni", input_formats=settings.DATE_INPUT_FORMATS,
                               widget=forms.DateInput(
                                   attrs={'class': 'form-control',
                                          'type': 'datetime-local',
                                          'placeholder': 'Masalan: 01.01.2020',
                                          'id': 'birthday'}))
    passport_seriya = forms.CharField(label='Passport seriyasi:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Masalan: AA', 'id': 'passport_seriya'}))
    passport_number = forms.IntegerField(label='Passport raqami:', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': 'Masalan: 1234567', 'id': 'passport_number'}))
    person_id = forms.IntegerField(label='JShShIR:', widget=forms.NumberInput(
        attrs={'class': 'form-control', 'placeholder': '14 xonali identifikatsiya raqamingizni kiriting...',
               'max': '99999999999999', 'min': '00000000000001', 'id': 'person_id'}))
    # phone = forms.IntegerField(label='Tel raqam:', widget=forms.NumberInput(attrs={'class': 'form-control','max': '999999999','min': '000000001','id': 'phone'}))
    region = forms.ModelChoiceField(queryset=Region.objects.all(), label="Viloyat:",
                                    widget=forms.Select(attrs={'class': 'form-control', 'id': 'region'}))
    district = forms.ModelChoiceField(queryset=District.objects.all(), label="Tuman/Shahar:",
                                      widget=forms.Select(attrs={'class': 'form-control', 'id': 'district'}))
    quarter = forms.ModelChoiceField(queryset=Quarter.objects.all(), label="Mahalla:",
                                 widget=forms.Select(attrs={'class': 'form-control', 'id': 'quarter'}))
    address = forms.CharField(label="Ko'cha/qishloq:", widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Masalan: Yangiyo'l ko'chasi 14-uy", 'id': 'address'}))
    # gender = forms.ChoiceField(label="Jins:", choices=GENDER_CHOICES,
    #                              widget=forms.Select(attrs={'class': 'form-control', 'id': 'gender'}))
    issue_by_whom = forms.CharField(label='Kim tomonidan berilgan:', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Masalan: BUXORO SHAHAR IIB', 'id': 'issue_by_whom'}))



    class Meta:
        model = User
        fields = ['last_name', 'first_name', 'middle_name', 'passport_seriya', 'passport_number',
                  'issue_by_whom', 'person_id', 'region', 'district', 'quarter', 'address']
        exclude = ['phone', 'birthday']

        labels = {
            'name': _('Writer'),
        }

        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
        }

        help_texts = {
            'person_id': 'Jismoniy shaxsning shaxsiy identifikatsion raqami'
        }
        error_messages = {
            'person_id': {
                'max_length': "This writer's name is too long."
            },
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].label = 'dsfdsfsdf'
        self.fields['first_name'].css_class = "label_required"

    def clean_email(self):
        email = self.cleaned_data['email']
        if not email:
            raise forms.ValidationError(u'Please enter an email address.')
        if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
            raise forms.ValidationError(u'Email "%s" is already in use.' % email)
        return email


class EditOrganizationForm(forms.ModelForm):
    title = forms.CharField(label='Tashkilot nomi:', widget=forms.TextInput(
        attrs={'class': 'form-control', }))
    director = forms.CharField(label='Rahbar:', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    identification_number = forms.IntegerField(label='STIR:', widget=forms.NumberInput(
        attrs={'class': 'form-control', }))
    legal_address_region = forms.ModelChoiceField(label='Yuridik manzil(Viloyat)', queryset=Region.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control' }))
    legal_address_district = forms.ModelChoiceField(label='Yuridik manzil(tuman)',queryset=District.objects.all(), widget=forms.Select(
        attrs={'class': 'form-control'}))
    address_of_garage = forms.CharField(label='Garaj manzili:', widget=forms.TextInput(
        attrs={'class': 'form-control'}))
    # certificate_photo = forms.FileField(label='Guvohnoma surati:', required=False, widget=forms.FileInput(
    #     attrs={'class': 'form-control-file',"accept": '.png, .jpg, .jpeg .gif' }))
    # license_photo = forms.FileField(label='Litsenziya surati:',required=False, widget=forms.FileInput(
    #     attrs={'class': 'form-control-file',"accept": '.png, .jpg, .jpeg .gif' }))

    class Meta:
        model = Organization
        fields = ['title', 'director', 'identification_number', 'legal_address_region','legal_address_district', 'address_of_garage',]
        # exclude = ['certificate_photo', 'license_photo']


# class AddCarForm(forms.ModelForm):
#
#     class Meta:
#         model = Car
#         fields = ['engine_number', 'body_number', 'color', 'made_year', 'address_of_garage',]
#         exclude = ['model', 'chassis_number', 'body_type', 'given_number', 'given_technical_passport']

class AddUserForm(ModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name','middle_name', )
        exclude = ('username', 'password',  'pasport','phone',)


class EditWorkerForm(ModelForm):

    class Meta:
        model = User
        fields = ('last_name', 'first_name', 'middle_name', 'section','region','district','quarter', 'address','passport_seriya','passport_number', 'username','turbo','password')
        exclude = ('phone',)

class EditCarForm(ModelForm):
    class Meta:
        model = Car
        fields = ('model','history', 'body_type', 'body_number','chassis_number', 'engine_number','made_year','color','engine_power','old_number','old_technical_passport','lost_technical_passport', 'type', 'fuel_type', 'device', 'is_auction', 'full_weight', 'empty_weight','is_old_number', 'lost_number' ,'given_number' )
        exclude = ()