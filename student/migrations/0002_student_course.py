# Generated by Django 5.0.6 on 2024-07-16 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='course',
            field=models.ManyToManyField(to='course.course'),
        ),
    ]