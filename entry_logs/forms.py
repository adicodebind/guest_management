from django import forms
from .models import VisitorLog
from base.validators import phone_number_validator


class VisitorLogForm(forms.Form):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(required=True, validators=[phone_number_validator])
    address = forms.CharField(required=True)


class CheckoutForm(forms.Form):
    email = forms.EmailField(required=True)
    token = forms.CharField(required=True)