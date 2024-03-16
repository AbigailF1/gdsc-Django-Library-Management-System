from django import forms
from django.contrib.auth.models import User
from . import models

class BookForm(forms.ModelForm):
    class Meta:
        model=models.Book
        fields=['book_name','book_isbn','book_author','book_category']