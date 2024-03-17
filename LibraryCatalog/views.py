from django.shortcuts import render, redirect
from .models import Book, Genre, Review
from .forms import BookForm, GenreForm, ReviewForm
from django.contrib import messages
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Avg



def book_added_view(request):
    return render(request, 'Book/bookadded.html')

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('book_added')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BookForm()
    return render(request, 'Book/addbook.html', {'form': form})


def list_all_authors(request):
    authors = Book.objects.values_list('author', flat=True).distinct()
    return render(request, 'Book/all_authors.html', {'authors': authors})

def search_books(request):
    query = request.GET.get('query')
    genre = request.GET.get('genre')
    author = request.GET.get('author')
    books = Book.objects.all()
    if query:
        books = books.filter(title__icontains=query)
    if author:
        books = books.filter(author__icontains=author)
    if genre:
        books = books.filter(genre__name=genre)
    return render(request, 'Book/search_results.html', {'books': books, 'query': query, 'selected_genre': genre})

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list') 
    else:
        form = GenreForm()
    return render(request, 'Book/add_genre.html', {'form': form})

def delete_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
    return redirect('genre_list')

def genre_list(request):
    genres=Genre.objects.all()
    return render(request, 'Book/genre_list.html', {'genres':genres})

def get_all_books(request):
    books=Book.objects.all()
    genres = Genre.objects.all()

    return render(request, 'Book/allbook.html', {'books':books, 'genres':genres})

def get_all_books_students(request):
    books=Book.objects.all()
    genres = Genre.objects.all()

    return render(request, 'Book/allbookstudents.html', {'books':books, 'genres':genres})

def get_book_by_id(request, pk):
    book=get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    return render(request, 'Book/book.html', {'book':book, 'reviews':reviews})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('get_all_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'Book/book_form.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('get_all_books')
    return render(request, 'Book/book_confirm_delete.html', {'book': book})

def submit_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.student = request.user
            review.book = book  # Assign the book object, not just the ID
            review.save()
            return redirect('book_review', book_id=book_id)
    else:
        form = ReviewForm()
    
    return render(request, 'Book/submit_review.html', {'form': form})

def book_review(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    reviews = Review.objects.filter(book=book)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'Book/book_review.html', {'book': book, 'reviews': reviews, 'average_rating': average_rating})

def delete_review(request, review_id):
    review = review = get_object_or_404(Review, id=review_id)
    if request.method == 'POST':
        review.delete()
        return redirect('Book/book_review', book_title=review.book.title)