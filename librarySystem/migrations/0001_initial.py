# Generated by Django 5.0.3 on 2024-03-11 14:49

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100, unique=True)),
                ('password', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('first_name', models.CharField(blank=True, max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, max_length=100, null=True)),
                ('role', models.CharField(max_length=100)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('is_banned', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('number_of_copies', models.IntegerField()),
                ('currently_available_copies', models.IntegerField()),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('genre', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarySystem.genre')),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('review_id', models.AutoField(primary_key=True, serialize=False)),
                ('review_text', models.TextField()),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('date', models.DateTimeField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.user')),
            ],
        ),
        migrations.CreateModel(
            name='BorrowedBook',
            fields=[
                ('borrowed_id', models.AutoField(primary_key=True, serialize=False)),
                ('borrowed_date', models.DateTimeField()),
                ('returned_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.book')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.user')),
            ],
        ),
    ]
