# Generated by Django 4.1.7 on 2023-09-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0010_neursemodel_neursetestmodel_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservemodel',
            name='bank',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AddField(
            model_name='reservemodel',
            name='melicod',
            field=models.CharField(default='0', max_length=150),
        ),
        migrations.AddField(
            model_name='reservemodel',
            name='trakingcod',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
