from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models import Avg
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

class Genre(models.Model):
    name = models.CharField(max_length=100)
    number_of_books = models.PositiveIntegerField(default=0) 

    def __str__(self):
        return f'{self.name} - {self.number_of_books}'

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)  
    number_of_copies = models.PositiveIntegerField(default=1)  
    currently_available_copies = models.PositiveIntegerField(default=1) 
    average_rating = models.DecimalField(max_digits=5, decimal_places=2, default=0.0) 

    def __str__(self):
        return self.title

    def update_average_rating(self):
        avg_rating = Review.objects.filter(book=self).aggregate(Avg('rating'))['rating__avg']
        self.average_rating = avg_rating or 0 
        self.save()

    def save(self, *args, **kwargs):
        if self.genre:
            self.genre.number_of_books += 1
            self.genre.save()
        super().save(*args, **kwargs)

    class Meta:
        unique_together = ('title', 'author')


@receiver(post_save, sender=Book)
def update_genre_book_count_on_create(sender, instance, created, **kwargs):
    if created:
        instance.genre.number_of_books += 1
        instance.genre.save()

@receiver(post_delete, sender=Book)
def update_genre_book_count_on_delete(sender, instance, **kwargs):
    instance.genre.number_of_books -= 1
    instance.genre.save()

class Review(models.Model):
    review_text = models.TextField()
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return f"{self.student.username} -> rating {self.rating}/10"
    class Meta:
        unique_together = ('student', 'book')

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.book.update_average_rating()
