# Generated by Django 4.1.3 on 2023-01-05 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Purchaseapp', '0009_orderedproductmodel_status_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderedproductmodel',
            name='status',
        ),
    ]
