# Generated by Django 2.1.13 on 2021-03-01 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_costing', '0004_grireview_grireviewhistory'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='grireview',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='grireviewhistory',
            name='created_by',
        ),
        migrations.AlterModelTable(
            name='grireviewhistory',
            table='GriReview_History',
        ),
    ]
