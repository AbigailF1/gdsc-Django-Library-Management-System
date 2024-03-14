from django.contrib import admin
from .models import Book, Review, Genre
from django.contrib.auth.models import Group

admin.site.site_header = 'Library Managment System Dashboard'

# admin.site.unregister(Group)
admin.site.register(Book)
admin.site.register(Review)
admin.site.register(Genre)