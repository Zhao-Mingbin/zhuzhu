from django.contrib import admin
from blog.models import *
# Register your models here.





class ArticleAdmin(admin.ModelAdmin):
	list_display = ('title','name','create_time')





admin.site.register(Article,ArticleAdmin)
