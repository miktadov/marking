from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
from decoder.views import base_args
from .models import *
from decoder.models import PdfFiles
from registration.models import Personal
from . import shablons as shb


def start(request, file_pk):
	if request.user.is_authenticated:
		pdf = PdfFiles.objects.get(pk=file_pk)
		if pdf.username != request.user.username:
			messages.error(request, 'Ошибка индексации файла. .  •_•"')
			return redirect('documents')
		args = base_args(request)
		args.setdefault('pdf', pdf)
		args.setdefault('files', AfterDocument.objects.filter(fk=pdf.pk).all())
		return render(request, 'sel_doc.html', args)
	else:
		return redirect('login')

def post(request):
	if request.method == 'POST' and request.user.is_authenticated:
		first = int(request.POST['first'])
		last = int(request.POST['last'])
		inbox = int(request.POST['inbox'])
		boxs = int(request.POST['boxs'])
		if boxs*inbox > last-first+1:
			messages.error(request, f'Вы пытаетесь создать {boxs} кор. по {inbox} км в каждой коробке. Это {boxs*inbox} км. Быбранный вами диапозон позваляет распечатать тллько {last-first+1} кодов.     ¿ •_• ?')
			return redirect('agr', request.POST['file'])
			
		type = request.POST['type']
		firstagr = int(request.POST['firstagr'])
		
		username = request.user.username
		pdf = PdfFiles.objects.get(pk=request.POST['file'])
		file = pdf.pdf_file_link[:-4]
		pers = Personal.objects.get(username=username)
		
		doc = AfterDocument()
		doc.count = last-first+1
		doc.username = username
		doc.first = first
		doc.last = last
		doc.type = type
		doc.fk = pdf

		if type == 'csv':
			doc.file = shb.csv(file, first, last)
			doc.comment = 'CSV в чистом виде'
		
		elif type == 'agr':
			pers.prefix = request.POST['prefix']
			pers.save()
			doc.comment = f'Агрег. {boxs}x{inbox}'
			doc.last = boxs*inbox+first-1
			doc.file = shb.agregaciya(file, first, boxs, inbox, firstagr, pers.inn, pers.prefix)

		elif type == 'contr':
			vsd = request.POST['vsd']
			doc_date = request.POST['doc_date']
			doc_numb = request.POST['doc_numb']
			doc_type = request.POST['doc_type']
			date_make = request.POST['date_make']
			tnvd = request.POST['tnvd']
			doc.comment = 'Ввод в об.'
			doc.file = shb.cont(file, first, last, pers.inn, vsd, doc_date, doc_numb, doc_type, date_make, tnvd)
			
		elif type == 'spis':
			doc.comment = 'Списание'
			doc.file = file

		elif type == 'otgr':
			doc.comment = 'Отгрузка'
			doc.file = file

		elif type == 'otgr_vivod':
			doc.comment = 'Отгрузка и вывод'
			doc.file = file

		elif type == 'vivod':
			doc.comment = 'Вывод из оборота'
			doc.file = file

		elif type == 'con':
			doc.comment = 'Контрактное производство РФ'
			doc.file = file
		
		doc.save()
		return redirect('agr', request.POST['file'])
	else:
		messages.error(request, 'Что то странное вы тут делаете.      •_•')
		return redirect('start')
	
