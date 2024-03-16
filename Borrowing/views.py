from django.shortcuts import render
from django.shortcuts import render
from .models import BorrowedBook

def borrowed_books(request):
    user = request.user
    borrowed_books = BorrowedBook.objects.filter(student=user)
    return render(request, 'Book/borrowedbook.html', {'borrowed_books': borrowed_books})
