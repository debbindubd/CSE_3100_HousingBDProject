from django import forms
from django.contrib.auth.models import User
from loginapp.models import UserInfo


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('facebook_id', 'profile_pic')