# Generated by Django 4.2.3 on 2023-07-13 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_image_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='bucket',
            name='items',
            field=models.ManyToManyField(to='app.item'),
        ),
        migrations.DeleteModel(
            name='BucketItem',
        ),
    ]