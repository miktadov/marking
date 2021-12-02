from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django import forms


class Authentication(AuthenticationForm):
	username = forms.CharField( label='Логин пользователя:',
														help_text='Логин должен быть уникальным',
														widget=forms.TextInput(
														attrs={'class':'form-control'}))
	password = forms.CharField( label='Пароль:',
														widget=forms.PasswordInput(
														attrs={'class':'form-control'}))


class RegistrationForm(UserCreationForm):
	username = forms.CharField( label='Логин пользователя:',
														help_text='Логин должен быть уникальным',
														widget=forms.TextInput(
														attrs={'class':'form-control'}))
	inn = forms.CharField( label='ИНН организации:',
														help_text='ИНН нужен для указания его в шаблонах.',
														widget=forms.TextInput(
														attrs={'class':'form-control',
																	'name':'inn',
																	'pattern':'[0-9]{10}',
																	'title':'Длина ИНН должна составлять 10 цифр.'}))
	email = forms.EmailField( label='Почта:',
														widget=forms.EmailInput(
														attrs={'class':'form-control'}))
	password1 = forms.CharField( label='Пароль:',
														help_text='Пароль должен содержать минимум 8 символов и содержать в себе цифры с латинскими буквали',
														widget=forms.PasswordInput(
														attrs={'class':'form-control',
																	'pattern':'{8}',
																	'title':'Должен сожержать цифры и буквы.'}))
	password2 = forms.CharField( label='Повтор пароля:',
														widget=forms.PasswordInput(
														attrs={'class':'form-control',
																	'pattern':'{8}'}))
#	prefix = forms.CharField( label='Префикс организации:',
#														help_text='Префикс нужен для указания его в шаблонах.',
#														widget=forms.TextInput(
#														attrs={'class':'form-control',
#																	'name':'prefix',
#																	'min':'7',
#																	'max':'10',
#																	'title':'Длина Префикса должна составлять от 7 до 10 цифр.'}))
	
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2')