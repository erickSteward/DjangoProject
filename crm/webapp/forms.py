from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput
from django.contrib.auth.models import User
from django import forms


# -Register/create a user
class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ['username', 'password1', 'password2']
        
# -Login a user
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())