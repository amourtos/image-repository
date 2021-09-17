from django import forms
from rufferuser.models import RufferUser
from django.core.exceptions import ValidationError

# -----------------------------------------------------------------------
# validators -----------------------------------------------------------


def validate_creds(value):
    if len(value) < 6:
        raise ValidationError(
            ('%(value)s is less than 8 characters'),
            params={'username': value}
        )
    if len(value) > 32:
        raise ValidationError(
            ('%(value)s is less than 8 characters'),
            params={'username': value}
        )
# -----------------------------------------------------------------------


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-control',
            "id": "exampleFormControlTextarea1",
            "placeholder": "username",
            'rows': '1',
        }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            "id": "exampleFormControlTextarea1",
            "placeholder": "",
            'rows': '1'
        }
    ))


class RegisterForm(forms.Form):
    username = forms.CharField(max_length=50, validators=[validate_creds])
    password = forms.CharField(
        widget=forms.PasswordInput, validators=[validate_creds])

    class Meta:
        model = RufferUser
        fields = ['username', 'password', 'email']
