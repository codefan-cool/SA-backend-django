# Generated by Django 2.1.13 on 2022-04-21 12:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0049_merge_20220420_1351'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='request_owner',
            field=models.ForeignKey(db_column='RequestOwner', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='request',
            name='submitted_by',
            field=models.ForeignKey(db_column='SubmittedBy', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),

    ]
