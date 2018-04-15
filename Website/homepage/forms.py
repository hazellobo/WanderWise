from django import forms
from django.contrib.auth.models import User
from .models import UserProfileInfo
from .models import CalculatePrice


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField(widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileInfoForm(forms.ModelForm):

    class Meta:
        model = UserProfileInfo
        fields = ('phone_number', 'first_name', 'last_name')


class CalculatePricePack(forms.ModelForm):

    class Meta:
        model = CalculatePrice
        fields = ('departure_city', 'adult', 'children', 'date_of_travel')
