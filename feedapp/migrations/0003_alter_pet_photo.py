# Generated by Django 5.1.2 on 2024-10-27 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedapp', '0002_pet_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='photo',
            field=models.ImageField(default='pet_photos/default.jpg', upload_to='pet_photos/'),
        ),
    ]
