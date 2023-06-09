# Generated by Django 4.1.7 on 2023-04-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accuntmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('melicode', models.IntegerField(default=0, max_length=10)),
                ('phonnumber', models.IntegerField(default=0, max_length=11)),
                ('berthday', models.DateField(max_length=100)),
                ('pasword', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='savecodphon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('melicode', models.IntegerField(default=0, max_length=10)),
                ('phonnumber', models.IntegerField(default=0, max_length=11)),
                ('berthday', models.CharField(max_length=100)),
                ('code', models.IntegerField(max_length=10)),
            ],
        ),
    ]
