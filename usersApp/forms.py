from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django import forms

from usersApp.models import User


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2',)

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}),
        }


class UserUpdateForm(UserChangeForm):
    password = forms.CharField(widget=forms.HiddenInput)

    class Meta:
        model = User
        fields = ('email', 'password', 'first_name', 'last_name', 'phone', 'avatar', 'country',)
