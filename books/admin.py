from django.contrib import admin
from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'publication_date', 'created_at')
    search_fields = ('title', 'author', 'genre')
    list_filter = ('genre', 'publication_date')

admin.site.register(Book, BookAdmin)