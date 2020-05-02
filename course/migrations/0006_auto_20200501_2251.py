# Generated by Django 3.0.5 on 2020-05-01 22:51

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_auto_20200501_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='chapter',
            field=smart_selects.db_fields.ChainedForeignKey(auto_choose=True, chained_field='course_name', chained_model_field='name_of_chapter', default='', on_delete=django.db.models.deletion.CASCADE, to='course.Chapter'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 22, 51, 27, 183426, tzinfo=utc)),
        ),
    ]
