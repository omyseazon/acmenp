# Generated by Django 4.0.2 on 2022-03-27 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SchoolApp', '0008_attendanceconfiguration_department_designation_role_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Product Name')),
                ('Stock', models.IntegerField()),
                ('Size', models.DecimalField(decimal_places=2, max_digits=30)),
                ('SellingPrice', models.DecimalField(decimal_places=2, max_digits=65, verbose_name='Selling Price')),
                ('Color', models.CharField(max_length=200, verbose_name='Color')),
                ('Status', models.CharField(choices=[('Active', 'Active'), ('Not Active', 'Not Active')], max_length=200)),
                ('AgeOrClass', models.CharField(max_length=200, verbose_name='Age Or Class')),
                ('Created', models.DateTimeField(auto_now_add=True, verbose_name='Created at ')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.productcategory', verbose_name='Category')),
            ],
        ),
        migrations.CreateModel(
            name='Purchase',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PurchaseType', models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit')], max_length=200, verbose_name='Purchase Type')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('ReceiptNumber', models.CharField(max_length=200, verbose_name='Receipt Number')),
                ('PurchaseDate', models.DateTimeField(auto_now_add=True, verbose_name='Purchase Date ')),
            ],
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('SaleType', models.CharField(choices=[('Cash', 'Cash'), ('Credit', 'Credit')], max_length=200, verbose_name='Sale Type')),
                ('ExpectedAmount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Expected Amount')),
                ('DiscountAmount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Discount Amount')),
                ('ActualAmount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Actual Amount')),
                ('ReceiptNumber', models.CharField(max_length=200, verbose_name='Receipt Number')),
                ('SaleDate', models.DateTimeField(auto_now_add=True, verbose_name='Sale Date ')),
                ('Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.productcategory', verbose_name='Category')),
                ('Student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.registeredstudent', verbose_name='Student')),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Supplier Name')),
                ('MobileNumber', models.CharField(max_length=200, verbose_name='Phone Number')),
                ('OpeningBalance', models.DecimalField(decimal_places=2, max_digits=65)),
                ('SellerName', models.CharField(max_length=200, verbose_name='Seller Name')),
                ('SellerPhone', models.CharField(max_length=200, verbose_name='Seller Phone')),
                ('EntryDate', models.DateTimeField(verbose_name='Entry Date')),
            ],
        ),
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200, verbose_name='Unit Name')),
                ('Number', models.IntegerField(verbose_name='Unit Number')),
            ],
        ),
        migrations.CreateModel(
            name='SaleItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField()),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Unit Price')),
                ('ExpectedAmount', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Expected Amount')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.product', verbose_name='Product')),
                ('Sale', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.sale', verbose_name='Sale')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BatchNumber', models.CharField(max_length=200, verbose_name='Batch Number')),
                ('Amount', models.DecimalField(decimal_places=2, max_digits=30)),
                ('Quantity', models.IntegerField()),
                ('UnitPrice', models.DecimalField(decimal_places=2, max_digits=30, verbose_name='Unit Price')),
                ('ExpiryDate', models.DateTimeField(auto_now_add=True, verbose_name='Expiry Date')),
                ('AlertDate', models.DateTimeField(auto_now_add=True, verbose_name='Alert Date')),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.product')),
                ('Purchase', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.purchase')),
            ],
        ),
        migrations.AddField(
            model_name='purchase',
            name='Supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.supplier', verbose_name='Supplier'),
        ),
        migrations.AddField(
            model_name='product',
            name='Unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='SchoolApp.unit', verbose_name='Unit'),
        ),
    ]