from django import from
from .models import user
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(forms.ModelForm):
    password1 = forms.CharField(widget =forms.PasswordInput)
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['email', 'username','password1','password2','first_name', 'last_name' ]


class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)
