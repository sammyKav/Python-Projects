# Generated by Django 2.1.5 on 2021-07-20 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_auto_20210716_1121'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('treat', 'treat'), ('entrees', 'entrees'), ('appetizers', 'appetizers'), ('drinks', 'drinks')], max_length=60),
        ),
    ]