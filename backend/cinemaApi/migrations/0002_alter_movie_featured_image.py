# Generated by Django 5.0.7 on 2024-08-08 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemaApi', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='movie_images/'),
        ),
    ]
