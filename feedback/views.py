from django.shortcuts import render, redirect
from .models import FeedBack
from django.contrib import messages

# Create your views here.

def feedback(request):
	if request.method == 'POST' and request.POST['coll_tel']:
		fb = FeedBack(colled=False)
		name = request.POST['coll_name']
		tel = request.POST['coll_tel']
		fb.name = name
		fb.tel = tel
		fb.save()
		messages.success(request, 'Спасибо что оставили заявку. В ближайшее время мы свяжемся с вами!')
		return redirect('start')
	else:
		messages.success(request, 'Так нельзя!')
		return redirect('start')
	