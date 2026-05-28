from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название книги')
    author = models.CharField(max_length=100, verbose_name='Автор')
    genre = models.CharField(max_length=50, verbose_name='Жанр')
    year = models.IntegerField(verbose_name='Год издания')
    description = models.TextField(verbose_name='Описание')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата добавления')

    def str(self):
        return self.title 