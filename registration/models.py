#pylint:disable=E0001
from django.db import models


class Personal(models.Model):
	username = models.CharField(max_length=30, verbose_name='Логин')
	inn = models.CharField(max_length=10, verbose_name='ИНН')
	balance = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Баланс')
	prefix = models.CharField(max_length=10, verbose_name='Префикс компании gs1')
	arg1 = models.CharField(max_length=250, blank=True)
	arg2 = models.CharField(max_length=250, blank=True)
	arg3 = models.CharField(max_length=250, blank=True)
	arg4 = models.CharField(max_length=250, blank=True)
	arg5 = models.CharField(max_length=250, blank=True)
	
	def __str__(self):
		return f'Логин: {self.username} - {self.balance}'
		
	
	
class Transactions(models.Model):
	data = models.DateTimeField(auto_now_add=True)
	inn = models.CharField(max_length=10, verbose_name='ИНН')
	sum = models.DecimalField(max_digits=9, decimal_places=2, verbose_name='Сумма операции')
	comment = models.CharField(max_length=200, verbose_name='Комментарий', blank=True)
	arg1 = models.CharField(max_length=250, blank=True)
	arg2 = models.CharField(max_length=250, blank=True)
	arg3 = models.CharField(max_length=250, blank=True)
	arg4 = models.CharField(max_length=250, blank=True)
	arg5 = models.CharField(max_length=250, blank=True)
	
	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		pers  = Personal.objects.get(inn=self.inn)
		pers.balance = float(pers.balance)+float(self.sum)
		pers.save()
	
	def __str__(self):
		return f'{self.inn} = {self.sum}'
	
	
	