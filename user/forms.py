from django import forms

from user.models import *


class SignUpForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'middle_name','birthday', 'person_id','phone', 'region', 'district', 'mfy', 'address',
                  'nationality', 'gender', 'document_issue', 'document_expiry', 'issue_by_whom']
        exclude = ['password', 'email', 'passport_seriya', 'passport_number']


class EditForm(forms.ModelForm):
    first_name = forms.CharField(label='Ism:',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Yoqubov', 'id': 'first_name'}))
    last_name = forms.CharField(label='Familiya:',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Sirojiddin', 'id': 'last_name'}))
    middle_name = forms.CharField(label='Otasining ismi:',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: Tojiddinovich', 'id': 'middle_name'}))
    birthday = forms.DateField(label="Tug'ilgan  kuni", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 01.01.2020', 'id': 'birthday'},format='%d.%m.%Y'))
    passport_seriya = forms.CharField(label='Passport seriyasi:', widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: AA','id': 'passport_seriya'}))
    passport_number = forms.IntegerField(label='Passport raqami:', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 1234567','id': 'passport_number'}))
    document_issue = forms.DateField(label="Passport berilgan sana:", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 01.01.2020', 'id': 'document_issue'},format='%d.%m.%Y'))
    document_expiry = forms.DateField(label="Passport amal qilish muddati:", widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: 01.01.2020', 'id': 'document_expiry'},format='%d.%m.%Y'))
    person_id = forms.IntegerField(label='JShShIR:', widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '14 xonali identifikatsiya raqamingizni kiriting...','max': '99999999999999','min': '00000000000001','id': 'person_id'}))
    # phone = forms.IntegerField(label='Tel raqam:', widget=forms.NumberInput(attrs={'class': 'form-control','max': '999999999','min': '000000001','id': 'phone'}))
    region = forms.ModelChoiceField(queryset=Region.objects.all(),label="Viloyat:", widget=forms.Select(attrs={'class': 'form-control','id': 'region'}))
    district = forms.ModelChoiceField(queryset=District.objects.all(),label="Tuman/Shahar:", widget=forms.Select(attrs={'class': 'form-control','id': 'district'}))
    mfy = forms.ModelChoiceField(queryset=MFY.objects.all(),label="Mahalla:", widget=forms.Select(attrs={'class': 'form-control','id': 'mfy'}))
    address = forms.CharField(label="Ko'cha/qishloq:", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Masalan: Yangiyo'l ko'chasi 14-uy", 'id': 'address'}))
    nationality = forms.ModelChoiceField(queryset=Nationality.objects.all(),label="Millati:", widget=forms.Select(attrs={'class': 'form-control', 'id': 'nationality'}))
    gender = forms.ChoiceField(label="Jins:", choices=GENDER_CHOICES,
                                 widget=forms.Select(attrs={'class': 'form-control', 'id': 'gender'}))
    issue_by_whom = forms.CharField(label='Kim tomonidan berilgan:',widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Masalan: BUXORO SHAHAR IIB', 'id': 'issue_by_whom'}))

    class Meta:
        model = User
        fields = ['last_name','first_name', 'middle_name','birthday','passport_seriya', 'passport_number','document_issue', 'document_expiry', 'issue_by_whom', 'person_id', 'region', 'district', 'mfy', 'address',
                  'nationality', 'gender', ]
        exclude = ['phone']

        # labels = {
        #     'name': _('Writer'),
        # }

        # widgets = {
        #     "first_name": forms.TextInput(attrs={"class": "form-control"}),
        # }
        #
        # help_texts = {
        #     'person_id': 'Jismoniy shaxsning shaxsiy identifikatsion raqami'
        # }
        # error_messages = {
        #     'person_id': {
        #         'max_length': "This writer's name is too long."
        #     },
        # }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['first_name'].label = 'dsfdsfsdf'
    #     self.fields['first_name'].css_class = "label_required"


    # def clean_email(self):
    #     email = self.cleaned_data['email']
    #     if not email:
    #         raise forms.ValidationError(u'Please enter an email address.')
    #     if User.objects.exclude(pk=self.instance.pk).filter(email=email).exists():
    #         raise forms.ValidationError(u'Email "%s" is already in use.' % email)
    #     return email