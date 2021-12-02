from django.contrib import admin
from registration.models import *


class TransactionsAdm(admin.ModelAdmin):
	list_display = ('inn', 'data', 'comment', 'sum')
	list_display_links = ('inn', )
	search_fields = ('inn', 'data', 'comment', 'sum')
	list_filter = ('data', 'sum')
	list_editable = ('comment', 'sum')
	list_per_page = 25
	list_max_show_all = 100
	

class PersonalAdm(admin.ModelAdmin):
	list_display = ('username', 'inn', 'balance', 'prefix')
	list_display_links = ('username', 'inn')
	search_fields = ('username', 'inn', 'balance', 'prefix')
	list_per_page = 25
	list_max_show_all = 100


admin.site.register(Personal, PersonalAdm)
admin.site.register(Transactions, TransactionsAdm)