from django.contrib import admin
from .models import News, News_Category

# Register your models here.
admin.site.register(News)
admin.site.register(News_Category)