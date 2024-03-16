from django import forms
from django.contrib.auth.models import User
from .models import BorrowedBook


class IssueBookForm(forms.Form):
    class Meta:
        model = BorrowedBook
        fields = ['book', 'return_date']  

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)