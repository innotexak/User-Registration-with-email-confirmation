from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=100, help_text='Required')
    profile_picture = forms.ImageField()
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        help_texts = {
                'username': None,
                'email': None,
                'password1':None, 
                'password2':None,  
            }


    # class Meta:
    #     model = User
    #     fields = ('username', 'email', 'password1', 'password2')