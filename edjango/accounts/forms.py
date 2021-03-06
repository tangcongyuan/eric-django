from django import forms
from accounts.models import Player
from django.contrib.auth.models import User

class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = Player
        fields = ('username', 'password')
        widgets =   {
                        'username': forms.fields.TextInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Username',
                                }),
                        'password': forms.widgets.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'placeholder': 'Password',
                                }),
                    }