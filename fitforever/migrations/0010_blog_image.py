# Generated by Django 2.2.4 on 2020-09-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitforever', '0009_remove_blog_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/Image'),
        ),
    ]