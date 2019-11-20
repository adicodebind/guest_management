from django.core import validators


def phone_number_validator(phone_number):
    try:
        phone_number = str(phone_number)
    except ValueError:
        raise validators.ValidationError('Invalid Input')

    if phone_number.isdigit() is False:
        raise validators.ValidationError('Phone numbers can only contain numbers')

    if not (10 <= len(phone_number) <= 11):
        raise validators.ValidationError('Length of phone number must be either 10 or 11')