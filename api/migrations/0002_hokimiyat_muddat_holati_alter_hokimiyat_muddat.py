# Generated by Django 4.2.4 on 2023-08-25 14:32

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hokimiyat',
            name='muddat_holati',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='hokimiyat',
            name='muddat',
            field=models.IntegerField(default=datetime.datetime(2023, 8, 26, 14, 32, 24, 200200, tzinfo=datetime.timezone.utc)),
        ),
    ]
