from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'year', 'description']

        labels = {
            'title': 'Название книги',
            'author': 'Автор',
            'genre': 'Жанр',
            'year': 'Год издания',
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
            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: 1943'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Краткое описание книги',
                'rows': 5
            }),
        }