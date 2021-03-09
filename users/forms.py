
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "Username",                
                "class"       : "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",
                "class"       : "form-control"
            }
        ))

class SignUpForm(UserCreationForm):

    username = forms.CharField(max_length=50, required=True,
        label='',
        help_text='Required. Inform unique username',
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username...'
        }))

    # first_name = forms.CharField(max_length=30, required=False,
    #     label='', help_text='Optional',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'First name...'
    #     }))

    # last_name = forms.CharField(max_length=30, required=False,
    #     label='', help_text='Optional',
    #     widget=forms.TextInput(attrs={
    #         'class': 'form-control',
    #         'placeholder': 'Last name...'
    #     }))

  
    email = forms.EmailField(max_length=254, required=True,
        label='', help_text='Required. Inform a valid email unique address.',
        widget=forms.EmailInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email...'
        }))


    password1 = forms.CharField(required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password...'
        }))

    password2 = forms.CharField(required=True,
        label='',
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Confirm password...'
        }))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')


