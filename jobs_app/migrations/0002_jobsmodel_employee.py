# Generated by Django 4.1.7 on 2023-06-27 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobsmodel',
            name='employee',
            field=models.CharField(default='مدیریت', max_length=150),
        ),
    ]
