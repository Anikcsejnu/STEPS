# Generated by Django 3.0.5 on 2020-05-13 15:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0012_auto_20200513_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 13, 15, 5, 0, 825564, tzinfo=utc)),
        ),
    ]
