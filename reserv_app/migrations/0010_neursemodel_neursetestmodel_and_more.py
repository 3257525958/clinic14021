# Generated by Django 4.1.7 on 2023-09-09 00:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reserv_app', '0009_reservemodel_pyment'),
    ]

    operations = [
        migrations.CreateModel(
            name='neursemodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mellicode', models.CharField(default='0', max_length=12)),
                ('inject_botax', models.CharField(default='0', max_length=150)),
                ('illnes', models.CharField(default='0', max_length=150)),
                ('drug', models.CharField(default='0', max_length=150)),
                ('sensivety', models.CharField(default='0', max_length=150)),
                ('pregnancy', models.CharField(default='0', max_length=150)),
                ('date_finaly', models.CharField(default='0', max_length=150)),
                ('image_full', models.CharField(default='0', max_length=150)),
                ('image_semi', models.CharField(default='0', max_length=150)),
                ('image_not', models.CharField(default='0', max_length=150)),
                ('satisfact', models.CharField(default='0', max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='neursetestmodel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mellicode', models.CharField(default='0', max_length=12)),
                ('inject_botax', models.CharField(default='0', max_length=150)),
                ('illnes', models.CharField(default='0', max_length=150)),
                ('drug', models.CharField(default='0', max_length=150)),
                ('sensivety', models.CharField(default='0', max_length=150)),
                ('pregnancy', models.CharField(default='0', max_length=150)),
                ('date_finaly', models.CharField(default='0', max_length=150)),
                ('image_full', models.CharField(default='0', max_length=150)),
                ('image_semi', models.CharField(default='0', max_length=150)),
                ('image_not', models.CharField(default='0', max_length=150)),
                ('satisfact', models.CharField(default='0', max_length=150)),
            ],
        ),
        migrations.AddField(
            model_name='reservemodeltest',
            name='mellicode',
            field=models.CharField(default='0', max_length=12),
        ),
    ]
