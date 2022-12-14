# Generated by Django 2.1.13 on 2022-06-29 15:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0018_auto_20220621_1737'),
        ('rrf', '0092_auto_20220623_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='InterlinerCosts',
            fields=[
                ('interliner_cost_id', models.BigAutoField(db_column='InterlinerCostID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('rate_sheet_id', models.TextField(db_column='RateSheetID', default=None, max_length=50, null=True)),
                ('rate_sheet_name', models.TextField(db_column='RateSheetName', default=None, max_length=4000, null=True)),
                ('vendor_id', models.TextField(db_column='VendorID', default=None, max_length=50, null=True)),
                ('as_rating', models.BooleanField(db_column='AsRating', default=False)),
                ('unit_symbol_id', models.BigIntegerField(db_column='UnitSymbolID', default=None)),
                ('unit_factor', models.DecimalField(db_column='UnitFactor', decimal_places=6, default=None, max_digits=19, null=True)),
                ('is_between', models.BooleanField(db_column='IsBetween', default=False)),
                ('customer_discount', models.DecimalField(db_column='CustomerDiscount', decimal_places=6, default=None, max_digits=19, null=True)),
                ('cost', models.TextField(db_column='Cost', default=None, max_length=4000, null=True)),
                ('destination_id', models.BigIntegerField(db_column='DestinationID', default=None)),
                ('origin_id', models.BigIntegerField(db_column='OriginID', default=None)),
                ('direction', models.TextField(db_column='Direction', default=None, max_length=50, null=True)),
                ('currency_id', models.ForeignKey(db_column='CurrencyID', on_delete=django.db.models.deletion.CASCADE, to='rrf.Currency')),
                ('destination_type_id', models.ForeignKey(db_column='DestinationTypeID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.PointType')),
                ('equipment_type_id', models.ForeignKey(db_column='EquipmentTypeID', on_delete=django.db.models.deletion.CASCADE, to='rrf.EquipmentType')),
                ('origin_type_id', models.ForeignKey(db_column='OriginTypeID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.PointType')),
                ('sub_service_level_id', models.ForeignKey(db_column='SubServiceLevelID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.SubServiceLevel')),
                ('unit_id', models.ForeignKey(db_column='UnitID', on_delete=django.db.models.deletion.CASCADE, to='pac.Unit')),
                ('weight_breaker_header_id', models.ForeignKey(db_column='WeightBreakHeaderID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.WeightBreakHeader')),
            ],
            options={
                'verbose_name_plural': 'InterlinerCosts',
                'db_table': 'InterlinerCosts',
            },
        ),
        migrations.CreateModel(
            name='InterlinerCostsHistory',
            fields=[
                ('version_num', models.IntegerField(db_column='VersionNum', default=None)),
                ('is_latest_version', models.BooleanField(db_column='IsLatestVersion', default=False)),
                ('updated_on', models.DateTimeField(db_column='UpdatedOn', default=None)),
                ('updated_by', models.TextField(db_column='UpdatedBy', default=None)),
                ('base_version', models.IntegerField(db_column='BaseVersion', default=None)),
                ('comments', models.TextField(db_column='Comments', default=None)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('rate_sheet_version_id', models.BigAutoField(db_column='RateSheetVersionID', primary_key=True, serialize=False)),
                ('rate_sheet_name', models.TextField(db_column='RateSheetName', default=None, max_length=4000, null=True)),
                ('vendor_id', models.TextField(db_column='VendorID', default=None, max_length=50, null=True)),
                ('as_rating', models.BooleanField(db_column='AsRating', default=False)),
                ('unit_symbol_id', models.BigIntegerField(db_column='UnitSymbolID', default=None)),
                ('unit_factor', models.DecimalField(db_column='UnitFactor', decimal_places=6, default=None, max_digits=19, null=True)),
                ('is_between', models.BooleanField(db_column='IsBetween', default=False)),
                ('customer_discount', models.DecimalField(db_column='CustomerDiscount', decimal_places=6, default=None, max_digits=19, null=True)),
                ('cost', models.TextField(db_column='Cost', default=None, max_length=4000, null=True)),
                ('destination_id', models.BigIntegerField(db_column='DestinationID', default=None)),
                ('origin_id', models.BigIntegerField(db_column='OriginID', default=None)),
                ('direction', models.TextField(db_column='Direction', default=None, max_length=50, null=True)),
                ('currency_version_id', models.ForeignKey(db_column='CurrencyVersionID', on_delete=django.db.models.deletion.CASCADE, to='rrf.CurrencyHistory')),
                ('destination_type_version_id', models.ForeignKey(db_column='DestinationTypeVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.PointTypeHistory')),
                ('equipment_type_version_id', models.ForeignKey(db_column='EquipmentTypeVersionID', on_delete=django.db.models.deletion.CASCADE, to='rrf.EquipmentTypeHistory')),
                ('origin_type_version_id', models.ForeignKey(db_column='OriginTypeVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.PointTypeHistory')),
                ('rate_sheet_id', models.ForeignKey(db_column='RateSheetID', on_delete=django.db.models.deletion.CASCADE, to='rrf.InterlinerCosts')),
                ('sub_service_level_version_id', models.ForeignKey(db_column='SubServiceLevelVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.SubServiceLevelHistory')),
                ('unit_version_id', models.ForeignKey(db_column='UnitVersionID', on_delete=django.db.models.deletion.CASCADE, to='pac.UnitHistory')),
                ('weight_break_header_version_id', models.ForeignKey(db_column='WeightBreakHeaderVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.WeightBreakHeaderHistory')),
            ],
            options={
                'verbose_name_plural': 'InterlinerCosts_History',
                'db_table': 'InterlinerCosts_History',
            },
        ),
        migrations.AlterIndexTogether(
            name='interlinercostshistory',
            index_together={('rate_sheet_id', 'version_num')},
        ),
    ]
