# Generated by Django 4.0.2 on 2022-03-29 22:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0016_rename_name_product_productname'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.productcategory', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='Amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=30, null=True),
        ),
        migrations.AlterField(
            model_name='purchase',
            name='PurchaseDate',
            field=models.DateField(verbose_name='Purchase Date '),
        ),
    ]
