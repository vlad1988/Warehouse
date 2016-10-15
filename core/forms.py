from django import forms
from django.contrib.auth.models import User

class LogInForm(forms.ModelForm):
	username = forms.CharField(required=True,label='Login')
	password = forms.CharField(required=True,label='Password', widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ['username', 'password']
