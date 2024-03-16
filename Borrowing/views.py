from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import BorrowedBook
from .forms import IssueBookForm

def borrowed_books(request):
    user = request.user
    borrowed_books = BorrowedBook.objects.filter(student=user)
    return render(request, 'Book/borrowedbook.html', {'borrowed_books': borrowed_books})


@login_required
def view_borrowed_books(request):
    user = request.user
    borrowed_books = BorrowedBook.objects.filter(student=user)
    return render(request, 'Book/view_borrowed_books_bythestudent.html', {'borrowed_books': borrowed_books})


@login_required
def issue_book(request):
    if request.method == 'POST':
        form = IssueBookForm(request.POST)
        if form.is_valid():
            student = request.user
            # Check if the student is authenticated and active
            if not student.is_active:
                messages.error(request, "Your account is not active.")
                return redirect('issue_book')
            # Check if the student has already borrowed three books
            if BorrowedBook.objects.filter(student=student).count() >= 3:
                messages.error(request, "You have already borrowed three books.")
                return redirect('issue_book')
            # Create a new entry in the BorrowedBook model
            borrowed_book = form.save(commit=False)
            borrowed_book.student = student
            borrowed_book.save()
            messages.success(request, "Book issued successfully.")
            return redirect(reverse('borrowed_books_by_student'))
    else:
        form = IssueBookForm()
    return render(request, 'issue_book.html', {'form': form})