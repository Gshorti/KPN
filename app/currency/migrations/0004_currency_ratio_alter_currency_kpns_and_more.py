# Generated by Django 4.2.13 on 2024-06-11 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_alter_currency_kpns_alter_currency_rubles'),
    ]

    operations = [
        migrations.AddField(
            model_name='currency',
            name='ratio',
            field=models.IntegerField(default=100),
        ),
        migrations.AlterField(
            model_name='currency',
            name='KPNS',
            field=models.FloatField(max_length=100000),
        ),
        migrations.AlterField(
            model_name='currency',
            name='Rubles',
            field=models.FloatField(max_length=100000),
        ),
    ]
