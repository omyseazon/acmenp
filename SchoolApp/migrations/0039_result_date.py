# Generated by Django 4.0.2 on 2022-04-05 13:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0038_remove_examination_marksto_remove_examination_point_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='Date',
            field=models.DateField(default=datetime.datetime(2022, 4, 5, 13, 26, 11, 784343, tzinfo=utc), verbose_name='End Date'),
        ),
    ]
