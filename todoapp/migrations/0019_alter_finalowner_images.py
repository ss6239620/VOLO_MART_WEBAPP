# Generated by Django 4.1.5 on 2023-02-18 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0018_alter_owner_images'),
    ]

    operations = [
        migrations.AlterField(
            model_name='finalowner',
            name='images',
            field=models.ImageField(upload_to='images'),
        ),
    ]