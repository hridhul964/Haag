# Generated by Django 5.1.4 on 2025-01-02 07:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Haagapp', '0013_rename_subject_teacher_model_address_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video_model',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Classvideo', models.FileField(blank=True, null=True, upload_to='classvideo/')),
                ('date', models.DateField(blank=True, null=True)),
                ('Description', models.CharField(blank=True, max_length=100, null=True)),
                ('amount', models.CharField(blank=True, max_length=100, null=True)),
                ('TEACHERID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Haagapp.teacher_model')),
            ],
        ),
    ]
