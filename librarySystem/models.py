from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_banned = models.BooleanField()
    def __str__(self):
        return self.username

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey('Genre', on_delete=models.SET_NULL, null=True, default=None)
    number_of_copies = models.IntegerField()
    currently_available_copies = models.IntegerField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.title

class BorrowedBook(models.Model):
    borrowed_id = models.AutoField(primary_key=True)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    student = models.ForeignKey('User', on_delete=models.CASCADE)
    borrowed_date = models.DateTimeField()
    returned_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.student} -> {self.book}"

class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    student = models.ForeignKey('User', on_delete=models.CASCADE)
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.student} -> rating {self.rating}/10"
    
class Genre(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

