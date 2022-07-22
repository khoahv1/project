from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
import re

class RegistratronForm(forms.Form):
    username = forms.CharField(label='Tai khoan', max_length=30)
    email = forms.EmailField(label='email')
    password1 = forms.CharField(label='Mat khau', widget=forms.PasswordInput())
    password2 = forms.CharField(label='Nhap lai mat khau', widget=forms.PasswordInput())

    def clean_password2(seft):
        if 'password1' in self.cleaned_data:
            password1 = self.cleaned_data['password1']
            password2 = self.cleaned_data['password2']
            if password1==password2 and password1:
                return password2
            raise forms.ValidationError('Mat khau khong hop le')

    def clean_username(self):
        username = cleaned_data['username']
        if not re.search(r'^\w+$', username):
            raise forms.ValidationError('Tai khoan co ky tu dac biet')
        try:
            User.objects.get(username = username)
        except ObjectDoesNotExist:
            return username
        raise forms.ValidationError('Tai khoan da ton tai')
