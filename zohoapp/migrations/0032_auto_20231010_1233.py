# Generated by Django 3.2.20 on 2023-10-10 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0031_auto_20231010_0857'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendor_table',
            name='bpin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor_table',
            name='bstreet',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor_table',
            name='spin',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='vendor_table',
            name='sstreet',
            field=models.CharField(default='', max_length=100),
        ),
    ]
