from django.db import models
from django.db.models import Avg
from django.core.validators import MinValueValidator, MaxValueValidator

from userManager.models import Student

# Create your models here.
class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, default=None)
    number_of_copies = models.IntegerField()
    currently_available_copies = models.IntegerField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)
    def __str__(self):
        return self.title
    def update_average_rating(self):
        avg_rating = Review.objects.filter(book=self).aggregate(Avg('rating'))['rating__avg']
        self.average_rating = avg_rating or 0 
        self.save()
    class Meta:
        unique_together = ('title', 'author')

    
class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    #student = models.ForeignKey(Student, on_delete=models.CASCADE)
    student = models.CharField(max_length=100) #change it with the above code when authenticated
    book = models.ForeignKey('Book', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.student} -> rating {self.rating}/10"
    
