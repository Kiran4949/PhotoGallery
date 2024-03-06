from django.forms import ModelForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms



class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True,label='Email', widget=forms.EmailInput(attrs= {'class' : 'form-control'} ))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs= {'class' : 'form-control'} ))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs= {'class' : 'form-control'} ))
   
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        widgets = {'username' : forms.TextInput(attrs= {'class': 'form-control' } )}