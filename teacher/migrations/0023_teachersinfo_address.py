# Generated by Django 2.1.8 on 2020-04-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0022_auto_20200424_1550'),
    ]

    operations = [
        migrations.AddField(
            model_name='teachersinfo',
            name='address',
            field=models.CharField(default='test', help_text='Enter your address', max_length=255),
        ),
    ]
