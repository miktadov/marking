from django.conf import settings
from datetime import datetime


def csv(file, first, last):
	link_old = settings.MEDIA_ROOT + '/' + file
	link_new = link_old + f'_csv_{str(datetime.now()).replace(":", "-")}.csv'.replace(" ", "-")
	csv_old = open(link_old+'.csv', 'r')
	csv_new = open(link_new, 'w')
	x = 1
	for i in csv_old:
		if x >= first and x <= last:
			csv_new.write(str(i[:-1]+'\r\n'))
		x += 1
	csv_new.close()
	csv_old.close()
	return link_new[link_new.find('account'):]
	
	
def agregaciya(file, first, boxs, inbox, first_serial_numb, inn, prefix):
	class SSCC:
		def __init__(self, first=0, prefix=''):
			self.prefix = prefix
			self.serial = first
			self.first = first
			self.sscc = ''
			print('create class')
			
		def get(self):
			if self.serial is self.first:
				self.next()
				return self.sscc
			else:
				return self.sscc
			
		def next(self):
			self.serial += 1
			modulo = self.mod(f'{self.prefix}{str(self.serial).zfill(7)}')
			self.sscc = modulo
			return self.sscc
			
		def mod(self, sscc):
			div1, div2, x = 0, 0, 1
			sc = reversed(list(sscc))
			for i in sc:
				if x%2 != 0:
					div1 += int(i)
				else:
					div2 += int(i)
				x += 1
			sum_mod = str(div1*3+div2)[-1]
			if sum_mod != '0':
				return f'{sscc}{10-int(sum_mod)}'
			else:
				return f'{sscc}{0}'
				
	s = SSCC(first=first_serial_numb-1, prefix=prefix)
	head = ['Тип документа,ИНН участника оборота товаров,Версия\n',
				  f'Документ на агрегацию,{inn},2\n',
				  'Параметры товаров\n',
				  'УИТУ,Вложеннный УИТ/УИТУ']
	link_old = settings.MEDIA_ROOT + '/' + file
	link_new = link_old + f'_agr_{str(datetime.now()).replace(":", "-")}.csv'.replace(" ", "-")
	csv_old = open(link_old+'.csv', 'r')
	csv_new = open(link_new, 'w')
	x=box=1
	for i in head:
		csv_new.write(i)
	code = ''
	for i in csv_old:
		if x >= first and x < boxs*inbox+first:
			if box > inbox:
				box = 1
				s.next()
			box += 1
			code = i[:31]
			if ',' in code or '"' in code:
				code = '"'+code.replace('"', '""')+'"'
			
			csv_new.write('\n'+'0'+s.get()+','+code)
		elif x >= boxs*inbox+first:
			break
		x += 1
	csv_new.close()
	csv_old.close()
	return link_new[link_new.find('account'):]
	
	
def cont(file, first, last, inn, vsd, doc_date, doc_numb, doc_type, date_make, tnvd):
	head = ['ИНН производителя или импортера,ИНН собственника,Дата производства,Тип производственного заказа,Версия\n',
				  f'{inn},{inn},{date_make},{doc_type},3\n',
				  'Параметры товаров\n',
				  'КИ,КИТУ,Код ТН ВЭД ЕАЭС товара,Дата производства,Вид документа подтверждающего соответствие,Номер документа подтверждающего соответствие,Дата документа подтверждающего соответствие,Идентификатор ВСД']
	link_old = settings.MEDIA_ROOT + '/' + file
	link_new = link_old + f'_contr_{str(datetime.now()).replace(":", "-")}.csv'.replace(" ", "-")
	csv_old = open(link_old+'.csv', 'r')
	csv_new = open(link_new, 'w')
	x=1
	for i in head:
		csv_new.write(i)
	code = ''
	for i in csv_old:
		if x >= first and x <= last:
			code = i[:38]
			if ',' in code or '"' in code:
				code = '"'+code.replace('"', '""')+'"'
			csv_new.write('\n'+code+',,'+tnvd+','+date_make+','+doc_type+','+doc_numb+','+doc_date+','+vsd)
		elif x > last:
			break
		x += 1
	csv_new.close()
	csv_old.close()
	return link_new[link_new.find('account'):]