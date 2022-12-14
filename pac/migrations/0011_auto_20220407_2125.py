# Generated by Django 2.1.13 on 2022-04-08 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0010_auto_20210520_2039'),
    ]

    operations = [
        migrations.AddField(
            model_name='basingpoint',
            name='basing_point_code',
            field=models.CharField(db_column='BasingPointCode', default='Test', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='basingpoint',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='basingpointhistory',
            name='basing_point_code',
            field=models.CharField(db_column='BasingPointCode', default='Test', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='basingpointhistory',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='city_code',
            field=models.CharField(db_column='CityCode', default='Test', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='cityhistory',
            name='city_code',
            field=models.CharField(db_column='CityCode', default='Test', max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='cityhistory',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='country',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='countryhistory',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='province',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='provincehistory',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='region',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='regionhistory',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='terminal',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='terminalhistory',
            name='description',
            field=models.TextField(db_column='Description', max_length=50, null=True),
        ),
    ]
