# Generated by Django 4.1.7 on 2023-09-08 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0008_reservemodel_cardnumber'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservemodel',
            name='pyment',
            field=models.CharField(default='0', max_length=20),
        ),
    ]