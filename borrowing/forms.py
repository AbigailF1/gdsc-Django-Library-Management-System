from django import forms
from .models import BorrowedBook

class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = []  # No need to include any fields here

class ReturnBookForm(forms.ModelForm):
    class Meta:
        model = BorrowedBook
        fields = []  # No need to include any fields here
