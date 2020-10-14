# Generated by Django 2.2.4 on 2020-06-12 09:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fitforever', '0003_different_address_order_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='Paytm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=0)),
                ('number', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitforever.Users')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_id', models.IntegerField(default=0)),
                ('name', models.CharField(max_length=25)),
                ('card_no', models.IntegerField()),
                ('month', models.IntegerField()),
                ('year', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fitforever.Users')),
            ],
        ),
    ]
