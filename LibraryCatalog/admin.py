from django.contrib import admin
from .models import Book, Review, Genre
from django.contrib.auth.models import Group

admin.site.site_header = 'Library Managment System Dashboard'
class BookAdmin(admin.ModelAdmin):
    list_display = ['title' , 'author', 'genre', 'average_rating', 'number_of_copies', 'currently_available_copies']
    list_editable = ['currently_available_copies','number_of_copies', 'average_rating', 'genre', 'author']
    list_filter = ['genre']
    ordering = ['title', 'genre']
    list_per_page = 10
    
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['book', 'rating',  'review_text', 'student', 'date']
    list_per_page = 5
    ordering = ['book', 'rating']


class GenreAdmin(admin.ModelAdmin):
    list_display = ['name', 'number_of_books']
    list_per_page = 15
    ordering = ['name']

admin.site.register(Book, BookAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Genre, GenreAdmin)


    