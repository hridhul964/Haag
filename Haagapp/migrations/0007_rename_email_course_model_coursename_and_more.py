# Generated by Django 5.1.4 on 2024-12-30 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Haagapp', '0006_teacher_model_subject'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course_model',
            old_name='email',
            new_name='coursename',
        ),
        migrations.RenameField(
            model_name='course_model',
            old_name='gender',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='course_model',
            old_name='phoneno',
            new_name='duration',
        ),
        migrations.RenameField(
            model_name='course_model',
            old_name='name',
            new_name='type',
        ),
        migrations.RemoveField(
            model_name='course_model',
            name='password',
        ),
        migrations.AddField(
            model_name='course_model',
            name='enddate',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course_model',
            name='startdate',
            field=models.DateField(blank=True, null=True),
        ),
    ]
