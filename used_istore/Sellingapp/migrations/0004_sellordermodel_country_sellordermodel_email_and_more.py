# Generated by Django 4.1.3 on 2022-12-30 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Sellingapp', '0003_remove_sellproductordermodel_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='sellordermodel',
            name='country',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sellordermodel',
            name='email',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sellordermodel',
            name='postcode',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sellordermodel',
            name='state',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
