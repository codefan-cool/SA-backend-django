# Generated by Django 2.1.13 on 2020-12-15 04:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0015_requestsectionlanepricingpointimportqueue'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestsectionlanepricingpointimportqueue',
            name='uni_type',
            field=models.TextField(db_column='UniType', default='UNPROCESSED'),
        ),
    ]