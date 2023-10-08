from .models import *
from django import forms


class SignUpForm(forms.ModelForm):
    class Meta:
        model = RegisteredUsers
        fields = "__all__"
        widgets = {
            "password": forms.PasswordInput(),
        }


class LoginForm(forms.Form):
    userName = forms.CharField(max_length=100)
    password = forms.CharField(widget=forms.PasswordInput())
