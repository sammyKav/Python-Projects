# Generated by Django 2.1.5 on 2021-07-19 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profile', '0004_auto_20210719_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Mr.', 'Mr.'), ('non-binary', 'non-binary'), ('Ms.', 'Ms.')], max_length=20, null=True),
        ),
    ]
