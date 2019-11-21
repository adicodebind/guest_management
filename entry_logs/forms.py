from django import forms

from registration.models import Host
from .models import VisitorLog
from base.validators import phone_number_validator


class VisitorLogForm(forms.Form):
    first_name = forms.CharField(required=True)
    last_name=forms.CharField()
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, validators=[phone_number_validator])
    address = forms.CharField(required=True, widget=forms.TextInput)
    host = forms.ModelChoiceField(queryset=Host.objects.all(), required=True, widget=forms.Select)


class CheckoutForm(forms.Form):
    email = forms.EmailField(required=True)
    token = forms.CharField(required=True)
