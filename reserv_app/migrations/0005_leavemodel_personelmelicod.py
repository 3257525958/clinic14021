# Generated by Django 4.1.7 on 2023-07-28 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0004_leavemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='leavemodel',
            name='personelmelicod',
            field=models.CharField(default='0', max_length=11),
        ),
    ]