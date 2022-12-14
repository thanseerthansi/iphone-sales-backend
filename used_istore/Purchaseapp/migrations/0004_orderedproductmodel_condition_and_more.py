# Generated by Django 4.1.3 on 2022-12-06 04:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Purchaseapp', '0003_reviewmodel_images'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderedproductmodel',
            name='condition',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='orderedproductmodel',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='orderedproductmodel',
            name='storage',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
