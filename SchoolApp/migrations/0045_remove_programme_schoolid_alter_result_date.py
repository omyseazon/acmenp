# Generated by Django 4.0.2 on 2022-05-14 19:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0044_alter_result_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='programme',
            name='SchoolId',
        ),
        migrations.AlterField(
            model_name='result',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 5, 14, 19, 6, 46, 433347, tzinfo=utc), verbose_name='End Date'),
        ),
    ]
