# Generated by Django 2.2.4 on 2020-09-27 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitforever', '0013_auto_20200927_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/Image'),
        ),
    ]
