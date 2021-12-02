from django.shortcuts import render, redirect
from django.contrib import messages
from .models import *

# Create your views here.
def comment(request):
	try:
		com = Comment()
		com.author = request.POST['name']
		com.tel = request.POST['tel']
		com.text = request.POST['text']
		com.save()
		messages.success(request, 'Ваш комментарий успешно оставлен. Спасибо)')
	except:
		messages.success(request, 'Произошла техническая ошибка. Мы уже трудимся над ее исправлением.')
	return redirect('start')