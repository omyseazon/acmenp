# Generated by Django 4.0.2 on 2022-08-20 06:47

import datetime
from decimal import Decimal
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0002_aboutschool_attendanceconfiguration_average_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchaseitem',
            name='AlertDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Alert Date'),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='ExpiryDate',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Expiry Date'),
        ),
        migrations.AlterField(
            model_name='purchaseitem',
            name='UnitPrice',
            field=models.DecimalField(decimal_places=2, max_digits=30, validators=[django.core.validators.MinValueValidator(Decimal('0'))], verbose_name='Unit Price'),
        ),
        migrations.AlterField(
            model_name='result',
            name='Date',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 8, 20, 6, 47, 27, 262352, tzinfo=utc), verbose_name='End Date'),
        ),
        migrations.AlterField(
            model_name='role',
            name='RoleName',
            field=models.CharField(max_length=200, unique=True, verbose_name='Role '),
        ),
        migrations.CreateModel(
            name='AssignTeacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stream', models.CharField(max_length=200)),
                ('Course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.course', verbose_name='Class')),
                ('Staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.staff', verbose_name='Staff')),
                ('Subjects', models.ManyToManyField(to='SchoolApp.Subject', verbose_name='Subjects ')),
            ],
        ),
    ]