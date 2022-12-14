# Generated by Django 2.1.13 on 2022-04-08 01:26

from django.db import migrations
from django.db import connection

def update_codes(apps, schema_editor):
    cursor_update = connection.cursor()
    sql_update = "UPDATE bp SET bp.ZoneCode = LTRIM(STR(ZoneID)) FROM [dbo].[Zone] AS bp;"
    cursor_update.execute(sql_update)

    cursor_alter = connection.cursor()
    sql_alter = "ALTER TABLE [dbo].[Zone] ADD UNIQUE (ZoneCode);"
    cursor_alter.execute(sql_alter)

    cursor_update = connection.cursor()
    sql_update = "UPDATE bp SET bp.ZoneCode = LTRIM(STR(ZoneID)) FROM [dbo].[Zone_History] AS bp;"
    cursor_update.execute(sql_update)

    cursor_alter = connection.cursor()
    sql_alter = "ALTER TABLE [dbo].[Zone_History] ADD UNIQUE (ZoneCode);"
    cursor_alter.execute(sql_alter)

class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0035_auto_20220407_2125'),
    ]

    operations = [
         #Invoke update_codes
         migrations.RunPython(update_codes, reverse_code=migrations.RunPython.noop),
    ]
