# Generated by Django 4.1.5 on 2023-02-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoapp', '0016_alter_finalowner_images_alter_item_images_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='images',
            field=models.ImageField(upload_to='images'),
        ),
    ]
