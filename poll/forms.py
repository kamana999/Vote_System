from django import forms
from .models import *


class InsertCity(forms.ModelForm):
    class Meta:
        model = City
        fields = '__all__'


class ContestantForm(forms.ModelForm):
    class Meta:
        model = Contestant
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = Voter
        exclude = 'u_status',


class LoginForm(forms.Form):
    email = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput())


