# Generated by Django 2.1.8 on 2020-04-24 15:50

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0021_auto_20200424_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersinfo',
            name='summary_of_activites',
            field=django_mysql.models.ListTextField(models.CharField(max_length=100), size=100),
        ),
    ]
