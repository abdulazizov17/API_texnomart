
from django.contrib import admin

from texnomart.models import Category, Product, Image, Comment, AttributeKey, AttributeValue, ProductAttribute


# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title','slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}
    autocomplete_fields = ('users_like',)


admin.site.register(Image)
admin.site.register(Comment)
admin.site.register(AttributeKey)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)