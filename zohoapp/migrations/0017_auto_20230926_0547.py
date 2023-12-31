# Generated by Django 3.2.20 on 2023-09-26 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0016_journal_journalcomment_journalentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='creditnote',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='credititem',
            name='item_name',
            field=models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.additem'),
        ),
    ]
