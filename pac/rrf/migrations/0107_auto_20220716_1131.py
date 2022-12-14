# Generated by Django 2.1.13 on 2022-07-16 14:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0106_auto_20220716_1105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requestqueue',
            name='request',
        ),
        migrations.RemoveField(
            model_name='requestqueue',
            name='request_status_type',
        ),
        migrations.RemoveField(
            model_name='requestqueue',
            name='user',
        ),
        migrations.AlterIndexTogether(
            name='requestqueuehistory',
            index_together=set(),
        ),
        migrations.RemoveField(
            model_name='requestqueuehistory',
            name='request_queue',
        ),
        migrations.RemoveField(
            model_name='requestqueuehistory',
            name='request_status_type_version',
        ),
        migrations.RemoveField(
            model_name='requestqueuehistory',
            name='request_version',
        ),
        migrations.RemoveField(
            model_name='requestqueuehistory',
            name='user_version',
        ),
        migrations.DeleteModel(
            name='RequestQueue',
        ),
        migrations.DeleteModel(
            name='RequestQueueHistory',
        ),
    ]
