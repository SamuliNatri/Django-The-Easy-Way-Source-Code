# Generated by Django 3.1.4 on 2021-01-10 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todo_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='test_field',
            field=models.TextField(default=''),
        ),
    ]
