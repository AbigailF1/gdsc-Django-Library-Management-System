from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Genre(models.Model):
    name = models.CharField(max_length=100)
    number_of_books = models.PositiveIntegerField(default=0)  # Default value added

    def __str__(self):
        return f'{self.name} - {self.number_of_books}'

STATUS_CHOICE = (
    ('avilable', 'AVILABLE'),
    ('borrowed', "BORROWED")
)
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)  # Set null and blank to True
    number_of_copies = models.IntegerField(default=0)  # Default value added
    currently_available_copies = models.PositiveIntegerField(default=0)  # Default value added
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)  # Default value added
    isbn_id = models.IntegerField(default=0000)
    status = models.CharField(max_length=20, choices= STATUS_CHOICE, default='avilable')
    
    def __str__(self):
        return self.title

class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)  # Automatically set to the current date and time when created

    def __str__(self):
        return f"{self.student.username} -> rating {self.rating}/10"
