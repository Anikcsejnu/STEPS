# Generated by Django 3.0.5 on 2020-05-02 07:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0008_auto_20200502_0701'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 2, 7, 27, 57, 840653, tzinfo=utc)),
        ),
    ]
