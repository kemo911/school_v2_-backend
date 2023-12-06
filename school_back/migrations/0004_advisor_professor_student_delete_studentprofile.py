# Generated by Django 4.2.7 on 2023-12-03 21:37

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('school_back', '0003_studentprofile_dob'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advisor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=2)),
                ('office_location', models.CharField(max_length=255)),
                ('office_hours', models.JSONField(max_length=2555)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Advisor',
            },
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=2)),
                ('office_hours', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Professor',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dob', models.DateField(default=datetime.datetime(2023, 12, 3, 21, 37, 16, 706126))),
                ('address', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=255)),
                ('emergency_contact_number', models.CharField(max_length=255)),
                ('enrollment_date', models.DateField(default=datetime.datetime(2023, 12, 3, 21, 37, 16, 706149))),
                ('advisor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='school_back.advisor')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
        migrations.DeleteModel(
            name='StudentProfile',
        ),
    ]