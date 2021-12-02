from django.contrib import admin
from feedback.models import *


class FeedBackAdm(admin.ModelAdmin):
	list_display = ('data', 'name', 'tel', 'comment', 'colled')
	list_display_links = ('data', )
	search_fields = ('data', 'name', 'tel', 'comment')
	list_filter = ('data', 'colled')
	list_editable = ('name', 'tel', 'comment', 'colled')
	list_per_page = 25
	list_max_show_all = 100
	

admin.site.register(FeedBack, FeedBackAdm)
