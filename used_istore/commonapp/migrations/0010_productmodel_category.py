# Generated by Django 4.1.3 on 2022-12-21 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commonapp', '0009_productmodel_model_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='category',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]