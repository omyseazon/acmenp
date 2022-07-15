# Generated by Django 4.0.2 on 2022-04-01 21:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0035_alter_monthly_discount_alter_quarterly_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fee',
            name='Course',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.course', verbose_name='Class'),
        ),
        migrations.AlterField(
            model_name='monthly',
            name='Discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.feediscount', verbose_name='Discount'),
        ),
        migrations.AlterField(
            model_name='quarterly',
            name='Discount',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.feediscount'),
        ),
    ]