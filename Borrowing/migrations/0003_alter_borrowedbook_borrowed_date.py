# Generated by Django 5.0.2 on 2024-03-14 13:16

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Borrowing', '0002_alter_borrowedbook_book_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='borrowed_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]