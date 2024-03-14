from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ProfilePicture = models.ImageField(default='default.jpg', upload_to='images', null=True)
    total_books_borrowed = models.PositiveIntegerField(default=0)
    current_books_borrowed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.student.username}-Profile'
