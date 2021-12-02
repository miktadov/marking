#pylint:disable=C0301
from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from .models import *
from registration.models import *
from decoder import decoder as dec
from threading import Thread
from PyPDF2 import PdfFileReader


def base_args(request):
	if request.user.is_authenticated:
		personal = Personal.objects.get(username=request.user.username)
		args = {
			'personal': personal,
			'media': settings.MEDIA_URL,
			'static': settings.STATIC_ROOT}
	else:
		args = {}
	return args

def start(request):
	if request.user.is_authenticated:
		pers = Personal.objects.get(username=request.user.username)
		args = {
			'personal': pers,
			'files': PdfFiles.objects.filter(inn=pers.inn).all()}
		return render(request, 'documents.html', args)
	else:
		messages.info(request, 'Что бы посетить эту страницу, вам необходимо войти.')
		return redirect('login')


def balance(request):
	args = base_args(request)
	return render(request, 'balance.html', args)


def load_file(request):
	
	def convert(pdf_class, inn, price):
		link = dec.make_csv(str(pdf_class.pdf_file))
#		link = dec.make_csv_test(str(pdf_class.pdf_file))
		pdf_class.csv_file = str(link)
		pdf_class.save()
		Transactions(
			inn=inn,
			comment=f'Конвертация {pdf_class.count_pages} км',
			sum=-price).save()
		return redirect('documents')
		
	if request.method == 'POST':
		
		try:
			if str(request.FILES['file'])[-3:] != 'pdf':
				messages.error(request,'Необходим файл формата PDF.')
				return redirect('documents')
		except:
			messages.error(request,'Для начала надо выбрать файл.')
			return redirect('documents')
			
		pers = Personal.objects.get(username=request.user.username)
		pdf = PdfFileReader(request.FILES['file'])
		pages = pdf.getNumPages()
		price = pages*0.12
		minuts = int(pages*0.18/60)
		seconds = round(pages*0.18%60)
		if float(pers.balance) >= price:
			try:
				pdf_class = PdfFiles()
				pdf_class.pdf_file = request.FILES['file']
				pdf_class.inn = pers.inn
				pdf_class.username = pers.username
				pdf_class.count_pages = pages
				pdf_class.save()
				slowly = Thread(target=convert, args=(pdf_class, str(pers.inn), price))
				slowly.start()
				messages.info(request,f'PDF файл загружен. Дождитесь завершения конвертации. Ориентировачное время конвертации {minuts} мин. {seconds} сек..')
			except:
				messages.info(request,'Ошибка обработки файла. Автоматически отправлено сообщение об ошибке в службу поддержки.')
				
		else:
			messages.error(request,
			f'На вашем балансе не хватает средств для совершения операции. Ваш баланс = {pers.balance}₽. Операция требует {price}₽. Вам не хватает {round(float(pers.balance)-price,2)}₽')
	else:
		messages.error(request,
			'Вы не выбрали файл для загрузки. Пожалуйста, нажмите "Загрузить файл" и выберите PDF файл в открывшейся директории.')
	return redirect('documents')
	
