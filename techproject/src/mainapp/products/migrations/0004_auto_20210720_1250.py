# Generated by Django 2.1.5 on 2021-07-20 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_auto_20210720_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='type',
            field=models.CharField(choices=[('appetizers', 'appetizers'), ('drinks', 'drinks'), ('entrees', 'entrees'), ('treat', 'treat')], max_length=60),
        ),
    ]