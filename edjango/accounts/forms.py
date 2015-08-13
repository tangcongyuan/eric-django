from django import forms
from accounts.models import User

class UserLoginForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ('Email', 'Password')
        widgets =   {
                        'Email': forms.fields.EmailInput(attrs={
                                    'class': '',
                                    'placeholder': 'Email',
                                }),
                        'Password': forms.widgets.PasswordInput(attrs={
                                    'class': '',
                                    'placeholder': 'Password',
                                }),
                    }