# Generated by Django 3.1 on 2020-09-05 11:17

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_auto_20200829_2230'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviews',
            name='create_date',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2020, 9, 5, 12, 20, 10)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reviews',
            name='update_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
