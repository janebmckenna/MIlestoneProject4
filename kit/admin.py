from django.contrib import admin
from .models import Product, Category, Team, Team_subs

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'name',
        'category',
        'price',
        'image',
    )

    ordering = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name'
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Team)
admin.site.register(Team_subs)