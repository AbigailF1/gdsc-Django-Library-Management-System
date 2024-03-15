from django.urls import path
from .views import get_all_books, get_book_by_id, book_create, book_update, search_books, list_all_authors, add_genre, delete_genre, genre_list, delete_book, submit_review

urlpatterns = [
    path('', get_all_books, name='get_all_books'),
    path('detail/<int:pk>/', get_book_by_id, name='book_detail'),
    path('create/', book_create, name='book_create'),
    path('update/<int:pk>/', book_update, name='book_update'),
    path('search/', search_books, name='search_books'),
    path('authors/', list_all_authors, name='list_all_authors'),
    path('genre/add/', add_genre, name='add_genre'),
    path('genre/', genre_list, name='genre_list'),
    path('genre/<int:pk>/delete/', delete_genre, name='delete_genre'),
    path('book/<int:pk>/delete/', delete_book, name='delete_book'),
    path('book/<int:book_id>/submit_review/', submit_review, name='submit_review'),
]
