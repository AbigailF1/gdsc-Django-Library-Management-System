# Generated by Django 5.0.2 on 2024-03-17 04:06

import Borrowing.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Borrowing', '0004_rename_returned_date_borrowedbook_return_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrowedbook',
            name='return_date',
            field=models.DateTimeField(default=Borrowing.models.default_return_date),
        ),
    ]
