from django.contrib import admin
from django.contrib import admin
from . import models

@admin.register(models.Book) # i use decoraters to simplicty and fully function.
class Bookadmin(admin.ModelAdmin):
    list_display = ['title', 'genre', 'average_rating', 'author', 'book_id', 'number_of_copies', 'currently_available_copies']
    list_editable = ['currently_available_copies', 'average_rating', 'genre', 'author']
    ordering = ['title', 'genre']
    list_per_page = 10

@admin.register(models.User)
class Useradmin(admin.ModelAdmin):
    list_display = ['username', 'user_id', 'email', 'role', 'date_joined', 'is_banned', 'password'] # the password should display for simplicity to other team members
    list_per_page = 10

@admin.register(models.BorrowedBook)
class BorrowedBookadmin(admin.ModelAdmin):
    list_display = ['borrowed_id', 'book', 'student', 'borrowed_date', 'returned_date']
    list_editable = ['returned_date']
    list_per_page = 10
    ordering = ['borrowed_date', 'student']

@admin.register(models.Review)
class Reviewadmin(admin.ModelAdmin):
    list_display = ['book', 'review_id', 'review_text', 'rating', 'student', 'date']
    list_per_page = 5
    ordering = ['book', 'rating', 'review_id']

@admin.register(models.Genre)
class Genreadmin(admin.ModelAdmin):
    list_display = ['author', 'base_id']
    list_per_page = 15
    ordering = ['author']
    
