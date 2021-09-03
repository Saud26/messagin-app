from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.forms import UserCreationForm



class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    
    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'input', 'placeholder': 'Username', 'minlength':'4'}
        self.fields['email'].widget.attrs = {'class': 'input', 'placeholder': 'Email Address'}
        self.fields['password1'].widget.attrs = {'class': 'input', 'placeholder': 'Password'}
        self.fields['password2'].widget.attrs = {'class': 'input', 'placeholder': 'Confirm password'}


class SettingsForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super(SettingsForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs = {'class': 'input', 'placeholder': 'Username', 'minlength':'4'}
        self.fields['email'].widget.attrs = {'class': 'input', 'placeholder': 'Email Address'}