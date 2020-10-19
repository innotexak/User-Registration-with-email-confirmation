from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required', widget=forms.TextInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, help_text='Required', widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {
                'username': None,
                'email': None,
                'password1':None, 
                'password2':None,  
            }

class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(widget=forms.TextInput(
         attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control'
        }
))
    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')