import requests
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from django.contrib.auth import login, logout
from .models import *
from .forms import *
from comments.models import Comment
from decoder.views import base_args
from datetime import datetime
from time import sleep



def start(request):
	args = base_args(request)
	args.setdefault('comments', Comment.objects.all())
	return render(request, 'index.html', args)


def user_login(request):
	if request.user.is_authenticated:
		messages.info(request, '"Что бы войти, надо - выйти!" Восточная мубрость.')
		return redirect('start')
	if request.method == 'POST':
		form = Authentication(data=request.POST)
		if form.is_valid():
			user = form.get_user()
			login(request, user)
			return redirect('start')
		else:
			messages.error(request, 'Пользователь по введенным вами данным не найден.')
	else:
		form = Authentication()
	return render(request, 'login.html', {'form': form})
	
# МЕТОД ВЫХОДА
def user_logout(request):
	logout(request)
	messages.info(request, 'Мы будем скучать, приходите вскоре!')
	return redirect('start')
		
# РЕГИСТРАЦИЯ
def register(request):
	if request.user.is_authenticated:
		messages.error(request, 'Вы уже зарегистрированны. Выйдите из своего аккаунта для того, что бы зарегистрировать другой аккаунт.')
		return redirect('start')
		
		
	if request.method == 'POST':
		try:
			inn = str(request.POST['inn'])
			if len(inn) != 10:
				messages.error(request,f'Введенный вами ИНН не соответствует стандартам. Длина ИНН должна составлять 10 цифр. Длина вашего ИНН {len(inn)} цифр.')
				form = RegistrationForm(request.POST)
				return render(request, 'register.html', {'form': form})
			inn_db = Personal.objects.get(inn=inn)
			register_accept = True
		except:
			register_accept = False
		
		if register_accept:
			messages.error(request, 'Введенный вами ИНН уже есть в базе данных зарегистрированных пользователей. Обратитесь в тех поддержку если это ваш ИНН')
			form = RegistrationForm(request.POST)
			return render(request, 'register.html', {'form': form})
			
		form = RegistrationForm(request.POST)
		if form.is_valid():
			form.save()
			pers = Personal()
			pers.username = request.POST['username']
			pers.inn = request.POST['inn']
#			pers.prefix = request.POST['prefix']
			pers.balance = 1.20
			pers.save()
			messages.success(request, 'Регистрация прошла успешно. На вашем балансе есть 1.20₽ на который вы можете сконвертировать 10 км. Войдите в созданный аккаунт.')
			return redirect('login')
		else:
			messages.error(request, 'Что то пошло не так ... =[')
	else:
		form = RegistrationForm()
	return render(request, 'register.html', {'form': form})
	
def help(request):
	messages.error(request, 'Наш сайт находится на стадии разработки, приносим извинения за неудобства. Если у вас возникли трудности свяжитесь с нами в телеграмм @rumalatau')
	return redirect('start')
	
def buy(request):
	if request.user.is_authenticated:
		user = Personal.objects.get(username=request.user.username)
		trans_new = Transactions()
		trans_new.inn = user.inn
		trans_new.comment = f'{user.username} {user.inn} {datetime.now()} white'
		trans_new.sum = 0.00
		trans_new.save()
		return redirect(f'https://oplata.qiwi.com/create?publicKey=48e7qUxn9T7RyYE1MVZswX1FRSbE6iyCj2gCRwwF3Dnh5XrasNTx3BGPiMsyXQFNKQhvukniQG8RTVhYm3iPtozV1P6RbMrHwmhrTseFscvSPry2cXnekni55Vam7xmPSSQbx6nhwpiq8KGEjakBwx5f5ytdsWzpze8ninXWnXgBBW9Gs42UoVHDrFjyM&comment={trans_new.comment}&successUrl=https://pdf-csv.ru/afterbuy/')
	else:
		return redirect('start')
	
def afterbuy(request):
	
	api_access_token = 'a29da8087b39a1088b268eb3ba436684'
	my_login = '+79897123271'
		
	s = requests.Session()
	s.headers['authorization'] = 'Bearer ' + api_access_token  
	parameters = {'rows': '3'}
	for xx in [1, 2]:
		h = s.get('https://edge.qiwi.com/payment-history/v1/persons/'+my_login+'/payments', params = parameters)
		checks = json.loads(h.text)['data']
		for check in checks:
			amount = check['sum']['amount']
			com = check['comment']
			try:
				trans_have = Transactions.objects.get(comment=com)
				if trans_have:
					trans_have.comment = com[:-5]+'complited'
					trans_have.sum = float(amount)
					trans_have.save()
					messages.success(request, f'Ваша оплата успешно проведена. На ваш счет зачисленно {amount} ₽.')
					return redirect('documents')
			except:
				xx = xx
		sleep(5)
	messages.success(request, 'Ошибка поиска платежа в истории. Обратитесь в службу поддержки. Кнопка "помощь"')
	return redirect('documents')
	
	
def qiwi_in(request):
	if request.method == 'POST':
		post = request.POST['bill']
		trans_have = Transactions.objects.get(comment=post['comment'])
		if trans_have:
			trans_new = Transactions()
			trans_new.inn = post['comment'].split()[1]
			trans_new.comment = post['comment']+post['amount']['value']+"Уже есть такой перевод."
			trans_new.sum = 0.00
			trans_new.save()
		else:
			trans_new = Transactions()
			trans_new.inn = post['comment'].split()[1]
			trans_new.comment = post['comment']
			trans_new.sum = float(post['amount']['value'])
			trans_new.save()
	else:
		return redirect('start')
			