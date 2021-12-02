from django.db import models

# Create your models here.

class FeedBack(models.Model):
	data = models.DateTimeField(auto_now_add=True)
	name = models.CharField(max_length=50, verbose_name='Имя')
	tel = models.CharField(max_length=200, verbose_name='Телефон')
	colled = models.BooleanField(verbose_name='Обработана', blank=True)
	comment = models.TextField(verbose_name='Комментарий к заявке', blank=True)
	arg1 = models.CharField(max_length=250, blank=True)
	arg2 = models.CharField(max_length=250, blank=True)
	