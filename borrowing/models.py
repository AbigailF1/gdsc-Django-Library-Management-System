from django.db import models
from userManager.models import Student
from libraryCatalog.models import Book
# Create your models here.
class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} -> {self.book}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_average_rating()