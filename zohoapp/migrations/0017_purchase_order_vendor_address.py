# Generated by Django 4.2.7 on 2024-03-07 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0016_purchase_order_customer_source_supply'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase_order',
            name='vendor_address',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
