# Generated by Django 4.1.3 on 2023-11-20 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0014_alter_statusmodel_code_alter_statusmodel_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='modelnamemodel',
            name='model_name',
            field=models.TextField(blank=True),
        ),
    ]
