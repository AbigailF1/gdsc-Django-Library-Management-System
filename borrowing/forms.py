from django import forms
from .models import BorrowedBook
from libraryCatalog import Review

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = []  # No need to include any fields here

class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = []  # No need to include any fields here

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['review_text', 'rating','student']
