# Generated by Django 4.1.3 on 2022-12-03 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0003_statusmodel_code'),
        ('Purchaseapp', '0002_reviewmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewmodel',
            name='images',
            field=models.ManyToManyField(to='commonapp.imagemodel'),
        ),
    ]