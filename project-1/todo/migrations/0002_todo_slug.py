# Generated by Django 3.1.4 on 2021-01-06 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='slug',
            field=models.SlugField(max_length=100, null=True),
        ),
    ]
