from django import forms
from .models import *

class RegistrationForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','phone_no','email','password']

class LoginForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username','password']
