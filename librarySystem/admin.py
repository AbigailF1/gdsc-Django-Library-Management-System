from django.contrib import admin
from .models import User, Book, Review, Genre, BorrowedBook,StudentExtra,IssuedBook
# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Genre)
admin.site.register(BorrowedBook)
admin.site.register(StudentExtra)
admin.site.register(IssuedBook)
