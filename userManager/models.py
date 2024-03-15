from django.db import models

# Create your models here.
class Student(models.Model):
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)
    email = models.EmailField()
    first_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    role = models.CharField(max_length=100)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_banned = models.BooleanField(default=False)
    def __str__(self):
        return self.username
