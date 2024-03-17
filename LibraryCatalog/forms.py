from django import forms
from django.contrib.auth.models import User
from . import models
from .models import Review



class BookForm(forms.ModelForm):
    class Meta:
        model = models.Book
        fields = ['title', 'author', 'genre', 'number_of_copies', 'currently_available_copies', 'average_rating']

class GenreForm(forms.ModelForm):
    class Meta:
        model = models.Genre
        fields = ['name', 'number_of_books']


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'review_text']

