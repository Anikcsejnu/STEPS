# Generated by Django 3.0.5 on 2020-05-10 12:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_auto_20200510_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 10, 12, 26, 56, 189294, tzinfo=utc)),
        ),
    ]
