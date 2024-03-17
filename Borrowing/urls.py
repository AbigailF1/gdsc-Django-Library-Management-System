from django.urls import path
from . import views as borrowedbook_views

urlpatterns = [
    path('borrowedbooks/', borrowedbook_views.borrowed_books, name='borrowed_books'),
    path('borrowedbooksbystudent/', borrowedbook_views.view_borrowed_books, name='borrowed_books_by_student'),
    path('issuebook/<int:book_id>/', borrowedbook_views.issue_book, name='issue_book'),
    
   
]