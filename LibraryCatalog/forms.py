from django import forms
from django.contrib.auth.models import User
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'genre', 'number_of_copies', 'currently_available_copies', 'average_rating']

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['name', 'number_of_books']