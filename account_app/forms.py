from django import forms
from django.core import validators
from django.core.validators import ValidationError


def start_with_0(value):
    if value[0] != "0":
        raise forms.ValidationError("phone should start with 0")


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={"class": 'form-control py-4'}), validators=[start_with_0])
    password = forms.CharField(widget=forms.PasswordInput(attrs={"class": 'form-control py-4'}))

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone) != 11:
            raise ValidationError("Your phone number is short", code="invalid_phone",
                                  params={'value': f'{phone}'})
        return phone


class OtpLoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={"placeholder": '09xxxxxxxxx', 'class': 'form-control py-4'}),
                            validators=[start_with_0])

    def clean_phone(self):
        phone = self.cleaned_data.get("phone")
        if len(phone) > 11:
            #           We can use this code except of validators.MaxLenghtValidator
            raise ValidationError("entered phone number is not valid!", code="invalid_phone",
                                  params={'value': f'{phone}'})
        return phone


class CheckOtpForm(forms.Form):
    code = forms.CharField(widget=forms.TextInput(attrs={'class': "form-control text-center py-4", 'placeholder': 'کد را وارد کنید'}),
                           validators=[validators.MaxLengthValidator(4)])
