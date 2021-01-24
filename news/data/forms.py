from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from data.models import *

class CreateuserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','password1','password2']

class Addcat(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

class Addheadline(forms.ModelForm):
    class Meta:
        model = Headline
        fields = '__all__'