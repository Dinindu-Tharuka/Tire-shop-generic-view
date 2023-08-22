# Generated by Django 4.2.4 on 2023-08-19 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data', '0003_alter_stockitem_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stockitem',
            name='discount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
        migrations.AlterField(
            model_name='stockitemsinvoice',
            name='total_discount',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
