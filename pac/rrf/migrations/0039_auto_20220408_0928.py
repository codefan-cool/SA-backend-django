# Generated by Django 2.1.13 on 2022-04-08 12:28

from django.db import migrations, connection

# Method to insert values in ServiceMatrix required for PAC 2429
def insert_service_matrix_data(apps, schema_editor):
    cursor_update = connection.cursor()
    sql_insert = """
        INSERT INTO  [dbo].[ServiceMatrix] ( [IsActive],[IsInactiveViewable],[BasingPointID],[CountryID],[PostalCodeID],[ProvinceID],
        ,[RegionID],[ServicePointID],[ServiceTypeID],[SubServiceLevelID],[TerminalID],[ZoneID]) VALUES
        (1, 1, 1, NULL, NULL, NULL, NULL, NULL, 2, 1, NULL, NULL), 
        (1, 1, 1, NULL, NULL, NULL, NULL, NULL, 2, 2, NULL, NULL), 
        (1, 1, NULL, 1, NULL, NULL, NULL, NULL, 2, 1, NULL, NULL),
        (1, 1, NULL, 2, NULL, NULL, NULL, NULL, 4, 1, NULL, NULL),
        (1, 1, NULL, NULL, NULL, 4, NULL, NULL, 4, 1, NULL, NULL),
        (1, 1, NULL, NULL, NULL, 5, NULL, NULL, 2, 2, NULL, NULL),
        (1, 1, NULL, NULL, NULL, 6, NULL, NULL, 2, 1, NULL, NULL),
        (1, 1, NULL, NULL, NULL, 7, NULL, NULL, 4, 1, NULL, NULL),
        (1, 1, NULL, NULL, NULL, 8, NULL, NULL, 4, 1, NULL, NULL),
        (1, 1, NULL, NULL, NULL, NULL, 2, NULL, 2, 1, NULL, NULL),
        (1, 1, NULL, NULL, NULL, NULL, 3, NULL, 2, 1, NULL, NULL);
        """
    cursor_update.execute(sql_insert)

class Migration(migrations.Migration):
    dependencies = [
        ('rrf', '0038_requestsectionlane_is_flagged'),
    ]

    operations = [
        migrations.RunPython(insert_service_matrix_data),
    ]