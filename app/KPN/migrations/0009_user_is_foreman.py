# Generated by Django 4.2.13 on 2024-06-11 19:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KPN', '0008_user_foreman'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_foreman',
            field=models.BooleanField(default=False),
        ),
    ]
