from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from django.contrib.auth.models import User

class UserRegister(UserCreationForm):
    username = forms.CharField(label='UNIQUE NAME (maximal length is 30) ', max_length=30, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='EMAIL (must consist(@/./)) ', widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password1 = forms.CharField(label='PASSWORD (NOT qwerty12345 :) , at least 8ch) ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label='REPEAT PASSWORD ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class UserLogin(AuthenticationForm):
    username = forms.CharField(label='Name(Username of your account) ', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Passward(Entry password) ', widget=forms.PasswordInput(attrs={'class': 'form-control'}))