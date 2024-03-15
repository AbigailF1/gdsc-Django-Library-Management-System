from django.shortcuts import render, redirect
from .models import BorrowedBook
from django.utils import timezone

from libraryCatalog.models import Book
from .forms import ReviewForm

# Create your views here.

def borrow_book(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        # Check if the user already borrowed 3 books
        if request.user.borrowing_set.count() >= 3:
            return render(request, 'borrow_limit_exceeded.html')
        # Check if the book is available
        if book.status == 'available':
            borrowing = BorrowedBook(user=request.user, book=book)
            borrowing.save()
            book.status = 'borrowed'
            book.save()
            return redirect('book_detail', pk=book_id)
        else:
            return render(request, 'book_not_available.html')
    return render(request, 'borrow_confirm.html', {'book': book})

def return_book(request, borrowing_id):
    borrowing = BorrowedBook.objects.get(pk=borrowing_id)
    if request.user == borrowing.user:
        borrowing.return_date = timezone.now().date()
        borrowing.book.status = 'available'
        borrowing.book.save()
        borrowing.save()
    return redirect('borrowed_books_list')

def borrowed_books_list(request):
    borrowings = BorrowedBook.objects.filter(user=request.user)
    return render(request, 'borrowed_books_list.html', {'borrowings': borrowings})

def submit_review(request, book_id):
    book = Book.objects.get(pk=book_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = 'change_it'
            #review.student = request.user.student
            review.book = book
            review.save()
            return redirect('book_detail', pk=book_id)
    else:
        form = ReviewForm()
    return render(request, 'submit_review.html', {'form': form,'book':book})
