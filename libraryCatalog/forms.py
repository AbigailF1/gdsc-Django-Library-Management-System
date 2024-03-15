from django import forms
from .models import Book, Genre, Review

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre', 'number_of_copies', 'currently_available_copies', 'average_rating']

class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = ['name']

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating','student']
