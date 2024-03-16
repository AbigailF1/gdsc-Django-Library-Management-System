# Generated by Django 5.0.2 on 2024-03-16 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0002_studentextra'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminSignupRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('email', models.EmailField(max_length=254)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
