# Generated by Django 2.1.13 on 2022-06-08 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0013_auto_20220412_1423'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicepoint',
            name='service_point_code',
            field=models.CharField(db_column='ServicePointCode', default='', max_length=10),
        ),
        migrations.AddField(
            model_name='servicepointhistory',
            name='service_point_code',
            field=models.CharField(db_column='ServicePointCode', default='', max_length=10),
        ),
    ]
