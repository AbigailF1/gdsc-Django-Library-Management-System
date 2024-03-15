from django.contrib import admin
from .models import  BorrowedBook


class BorrowedBookAdmin(admin.ModelAdmin):
    list_display = ['book', 'student', 'borrowed_date', 'return_date']
    list_editable = ['return_date']
    list_per_page = 10
    ordering = ['borrowed_date', 'student']

admin.site.register(BorrowedBook, BorrowedBookAdmin)