# Generated by Django 4.0.4 on 2022-05-02 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schoolapp', '0003_rename_is_current_organization_teachersjobhistory_is_current_job_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teachersjobhistory',
            old_name='is_current_organization',
            new_name='is_current_JOB',
        ),
        migrations.RenameField(
            model_name='teachersjobhistory',
            old_name='school_id',
            new_name='school',
        ),
        migrations.RenameField(
            model_name='teachersjobhistory',
            old_name='teacher_id',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='students',
            name='photo',
            field=models.ImageField(default='https://pics.freeicons.io/uploads/icons/png/13997075391582988868-512.png', upload_to='photo/students/'),
        ),
    ]
