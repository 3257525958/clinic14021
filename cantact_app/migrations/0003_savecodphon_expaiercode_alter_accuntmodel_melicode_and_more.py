# Generated by Django 4.1.7 on 2023-04-20 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cantact_app', '0002_alter_accuntmodel_berthday'),
    ]

    operations = [
        migrations.AddField(
            model_name='savecodphon',
            name='expaiercode',
            field=models.CharField(default=2, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='accuntmodel',
            name='melicode',
            field=models.CharField(default='0', max_length=10),
        ),
        migrations.AlterField(
            model_name='accuntmodel',
            name='phonnumber',
            field=models.CharField(default='0', max_length=11),
        ),
        migrations.AlterField(
            model_name='savecodphon',
            name='code',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='savecodphon',
            name='melicode',
            field=models.CharField(default='0', max_length=20),
        ),
        migrations.AlterField(
            model_name='savecodphon',
            name='phonnumber',
            field=models.CharField(default='0', max_length=20),
        ),
    ]
