from django.urls import path
from .views import borrow_book, return_book, borrowed_books_list

urlpatterns = [
    path('borrow/<int:book_id>/', borrow_book, name='borrow_book'),
    path('return/<int:borrowing_id>/', return_book, name='return_book'),
    path('borrowed/', borrowed_books_list, name='borrowed_books_list'),
]

