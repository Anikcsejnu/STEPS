# Generated by Django 3.0.5 on 2020-05-10 12:24

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200510_1822'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 12, 24, 45, 907332, tzinfo=utc)),
        ),
    ]
