# Generated by Django 2.1.13 on 2020-12-12 19:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0013_importfile_rate_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestsectionlaneimportqueue',
            name='uni_type',
            field=models.TextField(db_column='UniType', default='UNPROCESSED'),
        ),
    ]
