# Generated by Django 4.2.4 on 2023-09-17 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('services_data', '0001_initial'),
        ('inventory_data', '0002_alter_item_item_category_alter_item_supplier'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('invoice_id', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('discount_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('sub_total', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('custome_item_value', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='BillPayment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('payment_methods', models.CharField(choices=[('select', 'Select'), ('cash', 'Cash'), ('cheque', 'Cheque'), ('credit_card', 'Credit Card'), ('credit', 'Credit'), ('multiple', 'multiple')], default='select', max_length=20)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_payments', to='billing_data.bill')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCreditCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('payeename', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bill_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_credit_card', to='billing_data.billpayment')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCredit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('due_date', models.DateField()),
                ('payeename', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bill_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_credit', to='billing_data.billpayment')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCheque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('cheque_no', models.CharField(max_length=50)),
                ('payeename', models.CharField(max_length=50)),
                ('bank', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=50)),
                ('cheque_date', models.DateField()),
                ('bill_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payment_cheques', to='billing_data.billpayment')),
            ],
        ),
        migrations.CreateModel(
            name='PaymentCash',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('payeename', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bill_payment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='payments_cash', to='billing_data.billpayment')),
            ],
        ),
        migrations.CreateModel(
            name='BillServises',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_services', to='billing_data.bill')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bill_services', to='services_data.employee')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='bill_services', to='services_data.service')),
            ],
        ),
        migrations.CreateModel(
            name='BillItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('qty', models.PositiveSmallIntegerField()),
                ('customer_discount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('customer_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bill_items', to='billing_data.bill')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='items', to='inventory_data.item')),
            ],
        ),
    ]
