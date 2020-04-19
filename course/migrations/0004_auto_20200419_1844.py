# Generated by Django 2.1.8 on 2020-04-19 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0003_auto_20200419_1842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='dept',
            field=models.CharField(choices=[('SCIENCE', 'Science'), ('BUSINESS STUDIES', 'Business Studies'), ('ENGLISH', 'English'), ('ICT', 'Ict')], default='SCIENCE', max_length=100),
        ),
        migrations.AlterField(
            model_name='course',
            name='level',
            field=models.CharField(choices=[('HSC', 'HSC'), ('SSC', 'SSC')], default='HSC', max_length=100),
        ),
    ]
