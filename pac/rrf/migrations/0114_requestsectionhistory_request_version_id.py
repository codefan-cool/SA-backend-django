# Generated by Django 2.1.13 on 2022-08-04 01:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0113_auto_20220803_2238'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestsectionhistory',
            name='request_version_id',
            field=models.ForeignKey(db_column='RequestVersionID', default=3, on_delete=django.db.models.deletion.CASCADE, to='rrf.RequestHistory'),
            preserve_default=False,
        ),
    ]
