from django.contrib import admin
from .models import Category, NewsModel

# Register your models here.
# admin.site.register(Category)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(NewsModel)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'publish_time', 'created_time']
    list_filter = ['title', 'created_time', 'status']
    prepopulated_fields = {'slug': ('title',)}
    date_hierarchy = 'publish_time'
    search_fields = ['title', 'body']
    ordering = ['status', 'publish_time']