# Generated by Django 2.1.13 on 2022-04-11 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0041_merge_20220411_1451'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestsectionlanehistory',
            name='is_flagged',
            field=models.BooleanField(db_column='IsFlagged', default=False, null=True),
        )
    ]