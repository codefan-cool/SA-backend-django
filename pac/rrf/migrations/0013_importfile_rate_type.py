# Generated by Django 2.1.13 on 2020-12-12 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0012_auto_20201208_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='importfile',
            name='rate_type',
            field=models.TextField(db_column='RateType', default='UNDEFINED'),
        ),
    ]
