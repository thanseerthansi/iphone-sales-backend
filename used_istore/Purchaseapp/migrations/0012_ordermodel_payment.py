# Generated by Django 4.1.3 on 2023-08-18 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchaseapp', '0011_orderedproductmodel_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ordermodel',
            name='payment',
            field=models.BooleanField(default=False),
        ),
    ]