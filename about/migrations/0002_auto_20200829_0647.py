# Generated by Django 3.1 on 2020-08-29 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='coolfact',
            name='plus',
            field=models.BooleanField(default=0),
        ),
        migrations.AlterField(
            model_name='coolfact',
            name='fact_name',
            field=models.CharField(max_length=50),
        ),
    ]
