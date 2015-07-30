from django import forms
from login.models import User

class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('Email', 'Password')
        widgets =   {
                        'Email': forms.fields.EmailInput(attrs={
                                    'class': '',
                                    'placeholder': '',
                                }),
                        'Password': forms.fields.HiddenInput(attrs={
                                    'class': '',
                                    'placeholder': '',
                                }),
                    }