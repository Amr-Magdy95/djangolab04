# Generated by Django 3.2.9 on 2021-11-12 17:58

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cast',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actor_actress', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=64, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, null=True)),
                ('title', models.CharField(blank=True, max_length=64, null=True)),
                ('date', models.DateField(default=datetime.date.today, verbose_name='Date')),
                ('posters', models.ImageField(upload_to='media')),
                ('cast', models.ManyToManyField(to='movie.Cast')),
                ('category', models.ManyToManyField(to='movie.Category')),
            ],
        ),
    ]
