# Generated by Django 3.1 on 2020-08-29 19:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='world_premiere',
            field=models.DateField(default=datetime.date.today, verbose_name='Премьера в мире'),
        ),
    ]