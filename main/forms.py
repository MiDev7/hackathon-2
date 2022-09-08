from django import forms
from django.db import models
from django.forms import ModelForm
from .models import *

class user(forms.Form):
    username = forms.CharField(label="Username", max_length=150, required=True)
    first_name = forms.CharField(label="First Name", max_length=150)
    last_name = forms.CharField(label="Last Name", max_length=150)
    email = forms.EmailField(max_length=250, required=True)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    