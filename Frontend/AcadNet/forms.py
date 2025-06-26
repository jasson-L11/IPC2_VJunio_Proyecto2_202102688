from django import forms

class XMLContentForm(forms.Form):
    file = forms.FileField(label='Upload XML File')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150, label='Username')
    password = forms.CharField(widget=forms.PasswordInput, label='Password')