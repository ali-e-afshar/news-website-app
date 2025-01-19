# accounting/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User


class RegistrationForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'mobile_number', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.mobile_number = self.cleaned_data['mobile_number']
        user.user_type = 3  # Site User
        if commit:
            user.save()
        return user
