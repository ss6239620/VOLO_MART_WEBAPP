# Generated by Django 4.1.3 on 2022-12-21 19:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0002_todolist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='todolist',
            name='name',
        ),
    ]
