# Generated by Django 5.0.3 on 2024-03-17 14:47

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LibraryCatalog', '0004_alter_book_average_rating'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('student', 'book')},
        ),
    ]
