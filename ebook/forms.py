from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
        # fields = ['title', 'content', 'is_published', 'category']
        # widgets = {
        #     'title': forms.TextInput(attrs={"class": "", }),
        #     'description': forms.Textarea(attrs={"class": "", "rows": 5}),
        # }


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "login_inputs"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "login_inputs"}))


class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Username', widget=forms.TextInput(attrs={"class": "login_inputs"}))
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "login_inputs"}))
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput(attrs={"class": "login_inputs"}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={"class": "login_inputs"}),)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')