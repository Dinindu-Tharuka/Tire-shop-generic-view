# Generated by Django 4.2.4 on 2023-08-14 13:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nic', models.CharField(max_length=12)),
                ('name', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('telephone', models.CharField(max_length=15)),
                ('designation', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('service_value', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
