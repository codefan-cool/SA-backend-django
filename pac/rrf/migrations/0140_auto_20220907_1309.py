# Generated by Django 2.1.13 on 2022-09-07 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0139_auto_20220907_1251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessorialheaderhistory',
            name='business_grouping',
            field=models.TextField(db_column='BusinessGrouping', default=None, null=True),
        ),
    ]