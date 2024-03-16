from django.db import models
from django.utils import timezone
from LibraryCatalog.models import Book
from User.models import User

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE ,null=True)
    student = models.ForeignKey(User, on_delete=models.CASCADE, null = True)
    borrowed_date = models.DateTimeField(default=timezone.now)  # Default to current time
    return_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
         return f"{self.student.username} ordered {self.book.title}"

    def save(self, *args, **kwargs):
        # Ensure that returned_date is not before borrowed_date
        if self.returned_date and self.borrowed_date and self.returned_date < self.borrowed_date:
            raise ValueError("Returned date cannot be before borrowed date")
        super().save(*args, **kwargs)