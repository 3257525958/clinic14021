# Generated by Django 4.1.7 on 2023-09-08 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0007_reservemodeltest'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservemodel',
            name='cardnumber',
            field=models.CharField(default='0', max_length=20),
        ),
    ]