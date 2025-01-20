from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=15)

    class Meta:
        model = CustomUser
        fields = ('username', 'mobile_number', 'password1', 'password2')
