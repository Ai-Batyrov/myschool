# Generated by Django 4.0.4 on 2022-04-26 17:00

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('schoolapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='parents',
            name='photo',
            field=models.ImageField(default='https://pics.freeicons.io/uploads/icons/png/13997075391582988868-512.png',
                                    upload_to='photo/parents/<id>'),
        ),
        migrations.AddField(
            model_name='students',
            name='photo',
            field=models.ImageField(default='https://pics.freeicons.io/uploads/icons/png/13997075391582988868-512.png',
                                    upload_to='photo/students/<id>'),
        ),
        migrations.AddField(
            model_name='teachers',
            name='photo',
            field=models.ImageField(default='https://pics.freeicons.io/uploads/icons/png/13997075391582988868-512.png',
                                    upload_to='photo/teachers/<id>'),
        ),
    ]
