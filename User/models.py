from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    student = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    ProfilePicture = models.ImageField(default='default.jpg', upload_to='images', null=True)
    total_books_borrowed = models.PositiveIntegerField(default=0)
    current_books_borrowed = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.student.username}-Profile'

class StudentExtra(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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