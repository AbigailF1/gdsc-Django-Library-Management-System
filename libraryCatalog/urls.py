from django.urls import path
from . import views as book_view

urlpatterns = [
    path('allbooks/', book_view.get_all_books, name='get_all_books'),
    path('allbooksStudent/', book_view.get_all_books_students, name='get_all_books_students'),
    path('detail/<int:pk>/', book_view.get_book_by_id, name='book_detail'),
    path('add/', book_view.add_book, name='book_create'),
    path('book-added/', book_view.book_added_view, name='book_added'),
    path('update/<int:pk>/', book_view.book_update, name='book_update'),
    path('search/', book_view.search_books, name='search_books'),
    path('authors/', book_view.list_all_authors, name='list_all_authors'),
    path('genre/add/', book_view.add_genre, name='add_genre'),
    path('genre/', book_view.genre_list, name='genre_list'),
    path('genre/<int:pk>/delete/', book_view.delete_genre, name='delete_genre'),
    path('book/<int:pk>/delete/', book_view.delete_book, name='delete_book'),
    path('review/<int:pk>/delete/', book_view.delete_review, name='delete_review'),
    path('book/<int:book_id>/book_review/', book_view.book_review, name='book_review'),
    path('submit_review/<int:book_id>/', book_view.submit_review, name='submit_review')
   
]