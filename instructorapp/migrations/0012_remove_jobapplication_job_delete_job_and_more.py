# Generated by Django 5.0.6 on 2025-03-19 13:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('instructorapp', '0011_jobapplication'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='jobapplication',
            name='job',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
        migrations.DeleteModel(
            name='JobApplication',
        ),
    ]
