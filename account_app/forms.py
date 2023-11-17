from django import forms
from django.core import validators
from django.core.validators import ValidationError


def start_with_0(value):
    if value[0] != "0":
        raise forms.ValidationError("phone should start with 0")


def eleven_numbers(value):
    if len(value) != 11:
        raise forms.ValidationError("شماره تماس باید 11 رقم باشد!")


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control py-4'}), validators=[start_with_0,
                                                                                                      eleven_numbers])
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control py-4'}))


class OtpLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": '09xxxxxxxxx', 'class': 'form-control py-4'}),
                            validators=[start_with_0, eleven_numbers])


class CheckOtpForm(forms.Form):
    code = forms.CharField(
        widget=forms.TextInput(attrs={'class': "form-control text-center py-4", 'placeholder': 'کد را وارد کنید'}),
        validators=[validators.MaxLengthValidator(4)])
