from django import forms
from django.core.validators import MinLengthValidator

from registration.models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(), validators=[MinLengthValidator(8)])
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'phone_number']

    def clean(self):
        cleaned_data = super().clean()

        email = cleaned_data.get("email")
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        existing_user = User.objects.filter(email=email).first()
        if existing_user and existing_user.host:
            self.add_error("email", "A Host with this email already exists. Please login to your account")

        elif password != confirm_password:
            self.add_error("confirm_password", "Both Passwords Do Not Match!")
