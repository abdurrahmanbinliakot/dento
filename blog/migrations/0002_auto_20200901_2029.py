# Generated by Django 3.1 on 2020-09-01 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='created_on',
            field=models.DateField(auto_now_add=True),
        ),
    ]
