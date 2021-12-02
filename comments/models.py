from django.db import models

# Create your models here.

class Comment(models.Model):
	data = models.DateTimeField(auto_now_add=True)
	author = models.CharField(max_length=20, verbose_name='Автор')
	tel = models.CharField(max_length=14, verbose_name='Телефон')
	text = models.TextField(verbose_name='Комментарий')
	arg1 = models.CharField(max_length=250, blank=True)
	arg2 = models.CharField(max_length=250, blank=True)
	arg3 = models.CharField(max_length=250, blank=True)
	arg4 = models.CharField(max_length=250, blank=True)
	arg5 = models.CharField(max_length=250, blank=True)
	
	def __str__(self):
		return f'{self.author}'
	
	
	