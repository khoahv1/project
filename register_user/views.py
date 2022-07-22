from django.shortcuts import render
import re
from django import forms
from register_user.models import Nguoidung
# from django.contrib.auth.models import User
# from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

def register_user(request):
     return render(request,'register_user.html')
def home(request):
    return render(request,'home.html')
def login_fail(request):
    return render(request,'login_fail.html')

def register_process(request):
    username = request.GET.get('username')
    email = request.GET.get('email')
    password = request.GET.get('password')
    # password2 = request.GET.get('password2')
    # if not (password == password2 and password):
    #     return forms.ValidationError('Password not valid')
    # elif not re.search(r'^\w+$', username):
    #     return forms.ValidationError('Username invalid')
    # else:
    dulieu = Nguoidung(
        username = username,
        email = email,
        password = password
    )
    dulieu.save()
    return render(request,'login.html')

# def clean_password2(self):
#     if 'password' in self.cleaned_data:
#         password = self.cleaned_data['password']
#         password2 = self.cleaned_data['password2']
#         if password == password2 and password:
#             return password
#     raise forms.ValidationError('Password not valid')
# def clean_username(self):
#     if not re.search(r'^\w+$', username):
#         raise forms.ValidationError('Username invalid')
#     try:
#         User.objects.get(username = username)
#     except ObjectDoesNotExist:
#         return username
#     raise forms.ValidationError('User exist')
# def save(self):
#     User.objects.creat_user(username = self.cleaned_data['username'], email = self.cleaned_data['email'], password = self.cleaned_data['password'])