# Generated by Django 2.2.4 on 2020-06-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fitforever', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='discount',
            field=models.FloatField(default=0),
        ),
    ]