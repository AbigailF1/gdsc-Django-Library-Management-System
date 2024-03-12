from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime,timedelta
from django.utils import timezone


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

class StudentExtra(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=40)
    branch = models.CharField(max_length=40)
    #used in issue book
    def __str__(self):
        return self.user.first_name+'['+str(self.enrollment)+']'
    @property
    def get_name(self):
        return self.user.first_name
    @property
    def getuserid(self):
        return self.user.id
    
def get_expiry():
     return datetime.today() + timedelta(days=15)
 
class IssuedBook(models.Model):
    enrollment = models.CharField(max_length=30)
    book_isbn=models.PositiveIntegerField(null=True)
    issuedate = models.DateField(auto_now=True)
    expirydate = models.DateField(default=get_expiry)

    def __str__(self):
        return self.enrollment


class Book(models.Model):
    catchoice= [
        ('education', 'Education'),
        ('entertainment', 'Entertainment'),
        ('comics', 'Comics'),
        ('biography', 'Biographie'),
        ('history', 'History'),
    ]
    book_id=models.AutoField(primary_key=True)
    book_name=models.CharField(max_length=30, null=True)
    book_isbn=models.PositiveIntegerField(null=True)
    book_author=models.CharField(max_length=40, null=True)  # Allow null temporarily
    book_category=models.CharField(max_length=30, choices=catchoice, default='education')
    
    def __str__(self):
        return str(self.book_name)+"["+str(self.book_isbn)+']'


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

