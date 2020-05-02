# Generated by Django 3.0.5 on 2020-05-01 20:24

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc
import smart_selects.db_fields


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200501_2003'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorial',
            name='chaper',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='chapter',
            field=smart_selects.db_fields.ChainedForeignKey(chained_field='course_name', chained_model_field='name__name_of_course', default='', on_delete=django.db.models.deletion.CASCADE, to='course.Chapter'),
        ),
        migrations.AlterField(
            model_name='tutorial',
            name='uploaded_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 20, 24, 43, 307830, tzinfo=utc)),
        ),
    ]
