# Generated by Django 4.1.3 on 2022-12-21 06:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0007_productmodel_model_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='model_name',
        ),
    ]
