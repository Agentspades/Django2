# Generated by Django 3.2.9 on 2021-12-01 00:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Forum', '0006_auto_20211201_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 1, 10, 43, 49, 477121)),
        ),
        migrations.AlterField(
            model_name='threadmodel',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2021, 12, 1, 10, 43, 49, 477121)),
        ),
    ]
