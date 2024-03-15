#add some validation
from django.shortcuts import get_object_or_404, redirect, render

# Create your views here.
from .models import Book, Genre, Review
from .forms import BookForm, GenreForm, ReviewForm

def book_create(request, pk=None):
    if pk:
        book = get_object_or_404(Book, pk=pk)
    else:
        book = None

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('get_all_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def list_all_authors(request):
    authors = Book.objects.values_list('author', flat=True).distinct()
    return render(request, 'all_authors.html', {'authors': authors})

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
    return render(request, 'search_results.html', {'books': books, 'query': query, 'selected_genre': genre})

def add_genre(request):
    if request.method == 'POST':
        form = GenreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('genre_list')  # Redirect to a URL displaying the list of genres
    else:
        form = GenreForm()
    return render(request, 'add_genre.html', {'form': form})

def delete_genre(request, pk):
    genre = get_object_or_404(Genre, pk=pk)
    if request.method == 'POST':
        genre.delete()
    return redirect('genre_list')

def genre_list(request):
    genres=Genre.objects.all()
    return render(request, 'genre_list.html', {'genres':genres})

def get_all_books(request):
    books=Book.objects.all()
    genres = Genre.objects.all()

    return render(request, 'allbook.html', {'books':books, 'genres':genres})

def get_book_by_id(request, pk):
    book=get_object_or_404(Book, pk=pk)
    reviews = Review.objects.filter(book=book)
    return render(request, 'book.html', {'book':book, 'reviews':reviews})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('get_all_books')
    else:
        form = BookForm(instance=book)
    return render(request, 'book_form.html', {'form': form})

def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('get_all_books')
    return render(request, 'book_confirm_delete.html', {'book': book})


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
