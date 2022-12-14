# Generated by Django 2.1.13 on 2022-08-04 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0112_auto_20220803_2219'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestinformation',
            name='request_number',
        ),
        migrations.RemoveField(
            model_name='requestinformationhistory',
            name='request_number',
        ),
        migrations.RemoveField(
            model_name='requestprofile',
            name='request_number',
        ),
        migrations.RemoveField(
            model_name='requestprofilehistory',
            name='request_number',
        ),
        migrations.AddField(
            model_name='requestsection',
            name='request_id',
            field=models.ForeignKey(db_column='RequestID', default=3, on_delete=django.db.models.deletion.CASCADE, to='rrf.Request'),
            preserve_default=False,
        ),
    ]
