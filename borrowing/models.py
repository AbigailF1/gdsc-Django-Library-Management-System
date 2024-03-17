from django.db import models
from django.utils import timezone
from LibraryCatalog.models import Book
from User.models import User
from datetime import timedelta

def default_return_date():
    return timezone.now() + timedelta(days=15)

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    borrowed_date = models.DateTimeField(default=timezone.now)  # Default to current time
    return_date = models.DateTimeField(default=default_return_date)

    def __str__(self):
         return f"{self.student.username} ordered {self.book.title}"
    class Meta:
        unique_together = ('student', 'book')
        
    def save(self, *args, **kwargs):
        if self.return_date and self.borrowed_date and self.return_date < self.borrowed_date:
            raise ValueError("Returned date cannot be before borrowed date")
        super().save(*args, **kwargs)
