from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'publication_date', 'description']

        labels = {
            'title': 'Название книги',
            'author': 'Автор',
            'genre': 'Жанр',
            'publication_date': 'Дата публикации',
            'description': 'Описание',
        }

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Маленький принц'
            }),
            'author': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Антуан де Сент-Экзюпери'
            }),
            'genre': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Сказка'
            }),
            'publication_date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание книги',
                'rows': 5
            }),
        }