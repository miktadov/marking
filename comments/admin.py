from django.contrib import admin
from comments.models import *


class CommentAdm(admin.ModelAdmin):
	list_display = ('author', 'data', 'tel', 'text')
	list_display_links = ('author',)
	search_fields = ('author', 'data', 'tel', 'text')
	list_per_page = 25
	list_max_show_all = 100


admin.site.register(Comment, CommentAdm)

# Register your models here.
