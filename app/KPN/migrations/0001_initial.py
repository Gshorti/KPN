# Generated by Django 4.2.13 on 2024-06-09 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Telegram_hash', models.CharField(max_length=100)),
                ('Telegram_ID', models.CharField(max_length=100)),
                ('Rubles', models.IntegerField()),
                ('KPNS', models.IntegerField()),
            ],
        ),
    ]
