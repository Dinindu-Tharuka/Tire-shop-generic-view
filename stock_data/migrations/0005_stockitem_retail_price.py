# Generated by Django 4.2.4 on 2023-08-19 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock_data', '0004_alter_stockitem_discount_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockitem',
            name='retail_price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=8),
            preserve_default=False,
        ),
    ]
