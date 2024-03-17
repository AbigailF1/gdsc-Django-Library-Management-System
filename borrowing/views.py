from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BorrowedBook
from .forms import IssueBookForm
from LibraryCatalog.models import Book
from datetime import datetime, timedelta
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import F


def borrowed_books(request):
    user = request.user
    borrowed_books = BorrowedBook.objects.filter(student=user)
    return render(request, 'Book/borrowedbook.html', {'borrowed_books': borrowed_books})

def all_borrowed_books(request):
    all_borrowed_books = BorrowedBook.objects.all()
    return render(request, 'Book/all_borrowed_books.html', {'borrowed_books': all_borrowed_books})

def return_book(request, borrowed_book_id):
    borrowed_book = BorrowedBook.objects.get(pk=borrowed_book_id)
    book = borrowed_book.book
    
    Book.objects.filter(pk=book.pk).update(currently_available_copies=F('currently_available_copies') + 1)
    
    borrowed_book.delete()
    
    return redirect('borrowed_books_by_student')

@login_required
def view_borrowed_books(request):
    user = request.user
    borrowed_books = BorrowedBook.objects.filter(student=user)
    return render(request, 'Book/view_borrowed_books_bythestudent.html', {'borrowed_books': borrowed_books})


@login_required
def issue_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return_date = None
    student = request.user
    borrowed = BorrowedBook.objects.filter(book=book, student=student).exists()

    if borrowed:
        return render(request, 'Book/issuebook.html', {'success_message': 'already borrowed', 'book': book, 'return_date': return_date})

    if request.method == 'POST':        
        if student.is_authenticated and student.is_active:
            if student.borrowedbook_set.count() < 3:
                if book.currently_available_copies > 0:
                    borrowed_book  = BorrowedBook.objects.create(book=book, student=student)
                    return_date = borrowed_book.borrowed_date + timedelta(days=15)
                    book.currently_available_copies -= 1
                    book.save()
                    return render(request, 'Book/issuebook.html', {'success_message': 'Book issued successfully', 'book': book, 'return_date': return_date})
                else:
                    return render(request, 'Book/issuebook.html', {'error_message': 'No copies available', 'book': book, 'return_date': return_date})
            else:
                return render(request, 'Book/issuebook.html', {'error_message': 'You have already borrowed three books', 'book': book, 'return_date': return_date})
        else:
            return render(request, 'Book/issuebook.html', {'error_message': 'You must be logged in and active to borrow a book', 'book': book , 'return_date': return_date})
    else:
        return render(request, 'Book/issuebook.html', {'book': book, 'return_date': return_date})
