from django import forms
from django.core import validators

# class NameForm(forms.Form):
#     your_name = forms.CharField(label="Your name", max_length=100)
#     your_dob = forms.DateField(label='Date Of Birth', widget=forms.TextInput(attrs={'type':'date'}))
#     your_email = forms.EmailField(label="Your Email", max_length=100)

class user_form(forms.Form):
    user_name = forms.CharField(required=True, label='Full Name', widget=forms.TextInput(attrs={'placeholder': 'Enter Your Full Name', 'style': 'width:300px'}), validators=[validators.MaxLengthValidator(10)])
    user_dob = forms.DateField(label='Date Of Birth', widget=forms.TextInput(attrs={'type':'date'}))
    user_email = forms.EmailField(label='User Email')
    boolean_field = forms.BooleanField()