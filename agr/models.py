from django.db import models
from django.conf import settings
from datetime import datetime
from decoder.models import PdfFiles
    
    
class AfterDocument(models.Model):
	data = models.DateTimeField(auto_now_add=True, verbose_name='Дата формирования')
	username = models.CharField(max_length=50, verbose_name='Логин пользователя')
	type = models.CharField(max_length=20, verbose_name='Тип файла')
	count = models.IntegerField(verbose_name='Количество КМ')
	first = models.IntegerField(verbose_name='Первый КМ')
	last = models.IntegerField(verbose_name='Последний КМ')
	comment = models.TextField(verbose_name='Дополнительное инфо')
	fk = models.ForeignKey(PdfFiles, models.CASCADE)
	file = models.FileField(verbose_name='Файл')
	arg1 = models.CharField(max_length=250, blank=True)
	arg2 = models.CharField(max_length=250, blank=True)
	arg3 = models.CharField(max_length=250, blank=True)
	arg4 = models.CharField(max_length=250, blank=True)
	arg5 = models.CharField(max_length=250, blank=True)
	
#	first
#	last
#	inn
#	type
#	inbox
#	boxs
#	firstagr