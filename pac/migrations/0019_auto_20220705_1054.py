# Generated by Django 2.1.13 on 2022-07-05 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0018_auto_20220621_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='external_tm_id',
            field=models.CharField(blank=True, db_column='ExternalTMID', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='accounthistory',
            name='external_tm_id',
            field=models.CharField(blank=True, db_column='ExternalTMID', max_length=100, null=True),
        ),
    ]
