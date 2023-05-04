from django.contrib import admin
from .models import Category, Book

admin.site.register(Category)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    raw_id_fields = ('category',)
