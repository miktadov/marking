from django.contrib import admin
from decoder.models import *


class PdfFilesAdm(admin.ModelAdmin):
	list_display = ('data', 'username', 'inn', 'file_name', 'count_pages')
	list_display_links = ('data', 'username', 'inn')
	search_fields = ('data', 'username', 'inn', 'file_name', 'count_pages')
	list_filter = ('data', )
	list_per_page = 25
	list_max_show_all = 100


admin.site.register(PdfFiles, PdfFilesAdm)