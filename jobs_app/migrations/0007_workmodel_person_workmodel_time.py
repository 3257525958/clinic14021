# Generated by Django 4.1.7 on 2023-07-01 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs_app', '0006_workmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='workmodel',
            name='person',
            field=models.CharField(default='من', max_length=150),
        ),
        migrations.AddField(
            model_name='workmodel',
            name='time',
            field=models.CharField(default='امروز', max_length=50),
        ),
    ]
