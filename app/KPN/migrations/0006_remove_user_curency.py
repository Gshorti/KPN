# Generated by Django 4.2.13 on 2024-06-10 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KPN', '0005_rename_kpns_user_kpсs'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='curency',
        ),
    ]
