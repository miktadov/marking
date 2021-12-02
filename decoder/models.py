from django.db import models
from django.conf import settings
from datetime import datetime


def content_file_name(instance, filename):
    return f'account_files/{instance.username}/{str(datetime.now()).replace(":", "-")}_pdf/{filename}'.replace(" ", "-")


class PdfFiles(models.Model):
	username = models.CharField(max_length=30, verbose_name='Логин')
	inn = models.CharField(max_length=10, verbose_name='ИНН')
	pdf_file = models.FileField(upload_to=content_file_name)
	file_name = models.CharField(max_length=200, verbose_name='Название файла')
	csv_file = models.CharField(max_length=250, verbose_name='csv файл')
	pdf_file_link = models.CharField(max_length=250, verbose_name='pdf файл')
	count_pages = models.IntegerField(verbose_name='Количество км')
	data = models.DateTimeField(auto_now_add=True)
	arg1 = models.CharField(max_length=250, blank=True)
	arg2 = models.CharField(max_length=250, blank=True)
	arg3 = models.CharField(max_length=250, blank=True)
	arg4 = models.CharField(max_length=250, blank=True)
	arg5 = models.CharField(max_length=250, blank=True)
	
	
	def save(self, *args, **kwargs):
		self.file_name = str(self.pdf_file)[str(self.pdf_file).rfind('/')+1:]
		self.pdf_file_link = str(self.pdf_file)
		super().save(*args, **kwargs)
	
	def __str__(self):
		return f'{self.username}'
		
		
