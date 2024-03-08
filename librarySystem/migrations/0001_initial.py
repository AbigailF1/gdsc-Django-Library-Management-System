# Generated by Django 5.0.3 on 2024-03-08 09:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('AVAILABLE', 'Available'), ('BORROWED', 'Borrowed'), ('RESERVED', 'Reserved')], max_length=100)),
                ('average_rating', models.DecimalField(decimal_places=2, max_digits=5)),
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
                ('is_banned', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('rating', models.IntegerField()),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.user')),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('borrowed_date', models.DateTimeField()),
                ('returned_date', models.DateTimeField(blank=True, null=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='librarySystem.user')),
            ],
        ),
    ]
