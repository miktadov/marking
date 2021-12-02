from django.contrib import admin
from agr.models import *


class AfterDocumentAdm(admin.ModelAdmin):
	list_display = ('data', 'username', 'type', 'count')
	list_display_links = ('data', 'username')
	search_fields = ('data', 'username', 'type', 'count')
	list_filter = ('data', 'type')
	list_per_page = 25
	list_max_show_all = 100


admin.site.register(AfterDocument, AfterDocumentAdm)