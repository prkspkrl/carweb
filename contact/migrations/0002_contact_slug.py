# Generated by Django 4.1.7 on 2023-03-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='slug',
            field=models.SlugField(blank=True, max_length=200),
        ),
    ]