# Generated by Django 3.1 on 2020-08-29 00:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about_discription', models.TextField(default='There is no Discriptions hear', max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='coolFact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('counter', models.IntegerField(default=0)),
                ('fact_name', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.TextField(max_length=10)),
                ('amount_of_skill', models.SmallIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=30)),
                ('designation', models.TextField(max_length=100)),
                ('photo', models.ImageField(upload_to='team_member_photo')),
                ('facebook_profile', models.URLField()),
                ('twitter_profile', models.URLField()),
                ('google_plus_profile', models.URLField()),
            ],
        ),
    ]
