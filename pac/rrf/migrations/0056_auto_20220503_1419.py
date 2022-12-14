# Generated by Django 2.1.13 on 2022-05-03 18:19

from django.db import migrations, models
import django.db.models.deletion



class Migration(migrations.Migration):

    dependencies = [
        ('pac', '0013_auto_20220412_1423'),
        ('rrf', '0055_merge_20220421_1756'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessorialDetentionOverride',
            fields=[
                ('acc_detention_override_id', models.BigAutoField(db_column='AccDetentionOverrideID', primary_key=True, serialize=False)),
                ('tm_detention_override_id', models.BigIntegerField(db_column='TMDetentionOverrideID', default=None)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('base_rate', models.BooleanField(db_column='BaseRate', default=False)),
                ('description', models.TextField(db_column='Description', default=None, max_length=40, null=True)),
                ('detention_type', models.TextField(db_column='DetentionType', default=None, max_length=10, null=True)),
                ('effective_from', models.DateTimeField(db_column='EffectiveFrom', default=None)),
                ('effective_to', models.DateTimeField(db_column='EffectiveTo', default=None)),
                ('exclude_closed_days_detention', models.TextField(db_column='ExcludeClosedDaysDetention', default=None, max_length=20, null=True)),
                ('exclude_closed_days_freetime', models.TextField(db_column='ExcludeClosedDaysFreeTime', default=None, max_length=20, null=True)),
                ('fb_based_date_field', models.TextField(db_column='FBBasedDateField', default=None, max_length=10, null=True)),
                ('free_time_unit', models.TextField(db_column='FreeTimeUnit', default=None, max_length=3, null=True)),
                ('freetime_unit_to_measure', models.TextField(db_column='FreeTimeUnitofMeasure', default=None, max_length=10, null=True)),
                ('inter_company', models.TextField(db_column='InterCompany', default=None, max_length=5, null=True)),
                ('late_no_bill', models.TextField(db_column='LateNoBill', default=None, max_length=5, null=True)),
                ('late_window', models.DecimalField(db_column='LateWindow', decimal_places=6, default=None, max_digits=19, null=True)),
                ('ltl_proration_method', models.TextField(db_column='LtlProrationMethod', default=None, max_length=10, null=True)),
                ('max_bill_time', models.DecimalField(db_column='MaxBillTime', decimal_places=6, default=None, max_digits=19, null=True)),
                ('min_bill_time', models.DecimalField(db_column='MinBillTime', decimal_places=6, default=None, max_digits=19, null=True)),
                ('free_times', models.TextField(db_column='FreeTimes', default=None, max_length=4000, null=True)),
                ('operations_code', models.TextField(db_column='OperationsCode', default=None, max_length=10, null=True)),
                ('payment_option', models.TextField(db_column='PaymentOption', default=None, max_length=10, null=True)),
                ('second_bill_rate', models.DecimalField(db_column='SecondBillRate', decimal_places=6, default=None, max_digits=19, null=True)),
                ('shipper', models.TextField(db_column='Shipper', default=None, max_length=10, null=True)),
                ('shipper_group', models.TextField(db_column='ShipperGroup', default=None, max_length=10, null=True)),
                ('origin_zone_type', models.TextField(db_column='OriginZoneType', default=None, max_length=10, null=True)),
                ('destination_zone_type', models.TextField(db_column='DestinationZoneType', default=None, max_length=40, null=True)),
                ('start_bill_rate', models.DecimalField(db_column='StartBillRate', decimal_places=6, default=None, max_digits=19, null=True)),
                ('start_option', models.TextField(db_column='StartOption', default=None, max_length=40, null=True)),
                ('stop_option', models.TextField(db_column='StopOption', default=None, max_length=40, null=True)),
                ('use_actual_time', models.BooleanField(db_column='UseActualTime', default=False)),
                ('warning_send', models.TextField(db_column='WarningSend', default=None, max_length=5, null=True)),
                ('warning_time', models.DecimalField(db_column='WarningTime', decimal_places=6, default=None, max_digits=19, null=True)),
                ('min_std_charge', models.DecimalField(db_column='MinStdCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_header_id', models.ForeignKey(db_column='AccHeaderID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialHeader')),
                ('currency_id', models.ForeignKey(db_column='CurrencyID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Currency')),
                ('destination_zone_id', models.ForeignKey(db_column='DestinationZoneID', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Zone')),
                ('equipment_type_id', models.ForeignKey(db_column='EquipmentTypeID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.EquipmentType')),
                ('free_time_id', models.ForeignKey(db_column='FreeTimeID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.FreeTime')),
                ('origin_zone_id', models.ForeignKey(db_column='ZoneID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Zone')),
            ],
            options={
                'db_table': 'AccessorialDetentionOverride',
            },
        ),
        migrations.CreateModel(
            name='AccessorialDetentionOverrideHistory',
            fields=[
                ('version_num', models.IntegerField(db_column='VersionNum', default=None)),
                ('is_latest_version', models.BooleanField(db_column='IsLatestVersion', default=False)),
                ('updated_on', models.DateTimeField(db_column='UpdatedOn', default=None)),
                ('updated_by', models.TextField(db_column='UpdatedBy', default=None)),
                ('base_version', models.IntegerField(db_column='BaseVersion', default=None)),
                ('comments', models.TextField(db_column='Comments', default=None)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('acc_detention_override_version_id', models.BigAutoField(db_column='AccDetentionOverrideVersionID', primary_key=True, serialize=False)),
                ('tm_detention_override_id', models.BigIntegerField(db_column='TMDetentionOverrideID', default=None)),
                ('base_rate', models.BooleanField(db_column='BaseRate', default=False)),
                ('description', models.TextField(db_column='Description', default=None, max_length=40, null=True)),
                ('detention_type', models.TextField(db_column='DetentionType', default=None, max_length=10, null=True)),
                ('effective_from', models.DateTimeField(db_column='EffectiveFrom', default=None)),
                ('effective_to', models.DateTimeField(db_column='EffectiveTo', default=None)),
                ('exclude_closed_days_detention', models.TextField(db_column='ExcludeClosedDaysDetention', default=None, max_length=20, null=True)),
                ('exclude_closed_days_freetime', models.TextField(db_column='ExcludeClosedDaysFreeTime', default=None, max_length=20, null=True)),
                ('fb_based_date_field', models.TextField(db_column='FBBasedDateField', default=None, max_length=10, null=True)),
                ('free_time_unit', models.TextField(db_column='FreeTimeUnit', default=None, max_length=3, null=True)),
                ('freetime_unit_to_measure', models.TextField(db_column='FreeTimeUnitofMeasure', default=None, max_length=10, null=True)),
                ('inter_company', models.TextField(db_column='InterCompany', default=None, max_length=5, null=True)),
                ('late_no_bill', models.TextField(db_column='LateNoBill', default=None, max_length=5, null=True)),
                ('late_window', models.DecimalField(db_column='LateWindow', decimal_places=6, default=None, max_digits=19, null=True)),
                ('ltl_proration_method', models.TextField(db_column='LtlProrationMethod', default=None, max_length=10, null=True)),
                ('max_bill_time', models.DecimalField(db_column='MaxBillTime', decimal_places=6, default=None, max_digits=19, null=True)),
                ('min_bill_time', models.DecimalField(db_column='MinBillTime', decimal_places=6, default=None, max_digits=19, null=True)),
                ('free_times', models.TextField(db_column='FreeTimes', default=None, max_length=4000, null=True)),
                ('operations_code', models.TextField(db_column='OperationsCode', default=None, max_length=10, null=True)),
                ('payment_option', models.TextField(db_column='PaymentOption', default=None, max_length=10, null=True)),
                ('second_bill_rate', models.DecimalField(db_column='SecondBillRate', decimal_places=6, default=None, max_digits=19, null=True)),
                ('shipper', models.TextField(db_column='Shipper', default=None, max_length=10, null=True)),
                ('shipper_group', models.TextField(db_column='ShipperGroup', default=None, max_length=10, null=True)),
                ('origin_zone_type', models.TextField(db_column='OriginZoneType', default=None, max_length=10, null=True)),
                ('destination_zone_type', models.TextField(db_column='DestinationZoneType', default=None, max_length=40, null=True)),
                ('start_bill_rate', models.DecimalField(db_column='StartBillRate', decimal_places=6, default=None, max_digits=19, null=True)),
                ('start_option', models.TextField(db_column='StartOption', default=None, max_length=40, null=True)),
                ('stop_option', models.TextField(db_column='StopOption', default=None, max_length=40, null=True)),
                ('use_actual_time', models.BooleanField(db_column='UseActualTime', default=False)),
                ('warning_send', models.TextField(db_column='WarningSend', default=None, max_length=5, null=True)),
                ('warning_time', models.DecimalField(db_column='WarningTime', decimal_places=6, default=None, max_digits=19, null=True)),
                ('min_std_charge', models.DecimalField(db_column='MinStdCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_detention_override_id', models.ForeignKey(db_column='AccDetentionOverrideID', on_delete=django.db.models.deletion.CASCADE, to='rrf.AccessorialDetentionOverride')),
                ('acc_header_version_id', models.ForeignKey(db_column='AccHeaderVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialHeaderHistory')),
                ('currency_version_id', models.ForeignKey(db_column='CurrencyVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.CurrencyHistory')),
                ('destination_zone_version_id', models.ForeignKey(db_column='DestinationZoneVersionID', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.ZoneHistory')),
                ('equipment_type_version_id', models.ForeignKey(db_column='EquipmentTypeVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.EquipmentTypeHistory')),
                ('free_time_version_id', models.ForeignKey(db_column='FreeTimeVersionID', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.FreeTimeHistory')),
                ('origin_zone_version_id', models.ForeignKey(db_column='OriginZoneVersionID', default=None, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.ZoneHistory')),
            ],
            options={
                'db_table': 'AccessorialDetentionOverride_History',
            },
        ),
        migrations.CreateModel(
            name='AccessorialOverride',
            fields=[
                ('acc_override_id', models.BigAutoField(db_column='AccOverrideID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('tmacc_override_id', models.BigIntegerField(db_column='TMAccOverrideID', default=None)),
                ('allow_between', models.BooleanField(db_column='AllowBetween', default=False)),
                ('carrier_movement_type', models.TextField(db_column='CarrierMovementType', default=None, max_length=1, null=True)),
                ('acc_rate_custom_maximum', models.DecimalField(db_column='AccRateCustomMaximum', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_custom_minimum', models.DecimalField(db_column='AccRateCustomMinimum', decimal_places=6, default=None, max_digits=19, null=True)),
                ('description', models.TextField(db_column='Description', default=None, max_length=40, null=True)),
                ('effective_from', models.DateTimeField(db_column='EffectiveFrom', default=None, null=True)),
                ('effective_to', models.DateTimeField(db_column='EffectiveTo', default=None, null=True)),
                ('origin_zone_type', models.TextField(db_column='OriginZoneType', default=None, max_length=10, null=True)),
                ('destination_zone_type', models.TextField(db_column='DestinationZoneType', default=None, max_length=10, null=True)),
                ('acc_rate_dock', models.BooleanField(db_column='AccRateDock', default=False)),
                ('acc_rate_DOE_factorA', models.DecimalField(db_column='AccRateDOEFactorA', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_DOE_factorB', models.DecimalField(db_column='AccRateDOEFactorB', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_elevator', models.BooleanField(db_column='AccRateElevator', default=False)),
                ('acc_rate_exclude_legs', models.BooleanField(db_column='AccRateExcludeLegs', default=False)),
                ('acc_rate_extra_stop_rates', models.TextField(db_column='AccRateExtraStopRates', default=None, max_length=4000, null=True)),
                ('acc_rate_increment', models.DecimalField(db_column='AccRateIncrement', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_fuel_price_average', models.TextField(db_column='AccRateFuelPriceAverage', default=None, max_length=10, null=True)),
                ('acc_rate_max_charge', models.DecimalField(db_column='AccRateMaxCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_min_charge', models.DecimalField(db_column='AccRateMinCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_percent', models.DecimalField(db_column='AccRatePercent', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_field2ID', models.BigIntegerField(db_column='AccRateRangeField2ID', default=None)),
                ('acc_rate_range_from1', models.DecimalField(db_column='AccRateRangeFrom1', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_to1', models.DecimalField(db_column='AccRateRangeTo1', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_from2', models.DecimalField(db_column='AccRateRangeFrom2', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_to2', models.DecimalField(db_column='AccRateRangeTo2', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_shipping_instructionID', models.BigIntegerField(db_column='AccRateShippingInstructionID', default=None, null=True)),
                ('acc_rate_survey', models.BooleanField(db_column='AccRateSurvey', default=False)),
                ('acc_rate_stairs', models.BooleanField(db_column='AccRateStairs', default=False)),
                ('acc_rate_status_code', models.TextField(db_column='AccRateStatusCode', default=None, max_length=10, null=True)),
                ('acc_rate_threshold_amount', models.DecimalField(db_column='AccRateThresholdAmount', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_vehicle_restricted', models.BooleanField(db_column='AccRateVehicleRestricted', default=False)),
                ('min_std_charge', models.DecimalField(db_column='MinStdCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_header_id', models.ForeignKey(db_column='AccHeaderID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialHeader')),
                ('acc_rate_factor_id', models.ForeignKey(db_column='AccRateFactorID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccFactor')),
                ('acc_rate_range_field1ID', models.ForeignKey(db_column='AccRangeTypeID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccRangeType')),
                ('commodity_id', models.ForeignKey(db_column='CommodityID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Commodity')),
                ('destination_zone_id', models.ForeignKey(db_column='DestinationZoneID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Zone')),
                ('origin_zone_id', models.ForeignKey(db_column='OriginZoneID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Zone')),
            ],
            options={
                'db_table': 'AccessorialOverride',
            },
        ),
        migrations.CreateModel(
            name='AccessorialOverrideHistory',
            fields=[
                ('version_num', models.IntegerField(db_column='VersionNum', default=None)),
                ('is_latest_version', models.BooleanField(db_column='IsLatestVersion', default=False)),
                ('updated_on', models.DateTimeField(db_column='UpdatedOn', default=None)),
                ('updated_by', models.TextField(db_column='UpdatedBy', default=None)),
                ('base_version', models.IntegerField(db_column='BaseVersion', default=None)),
                ('comments', models.TextField(db_column='Comments', default=None)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('acc_override_version_id', models.BigAutoField(db_column='AccOverrideVersionID', primary_key=True, serialize=False)),
                ('tmacc_override_id', models.BigIntegerField(db_column='TMAccOverrideID', default=None)),
                ('acc_header_version_id', models.BigIntegerField(db_column='AccountHeader', default=None)),
                ('allow_between', models.BooleanField(db_column='AllowBetween', default=False)),
                ('carrier_movement_type', models.TextField(db_column='CarrierMovementType', default=None, max_length=1, null=True)),
                ('acc_rate_custom_maximum', models.DecimalField(db_column='AccRateCustomMaximum', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_custom_minimum', models.DecimalField(db_column='AccRateCustomMinimum', decimal_places=6, default=None, max_digits=19, null=True)),
                ('description', models.TextField(db_column='Description', default=None, max_length=40, null=True)),
                ('effective_from', models.DateTimeField(db_column='EffectiveFrom', default=None, null=True)),
                ('effective_to', models.DateTimeField(db_column='EffectiveTo', default=None, null=True)),
                ('origin_zone_type', models.TextField(db_column='OriginZoneType', default=None, max_length=10, null=True)),
                ('destination_zone_type', models.TextField(db_column='DestinationZoneType', default=None, max_length=10, null=True)),
                ('acc_rate_dock', models.BooleanField(db_column='AccRateDock', default=False)),
                ('acc_rate_DOE_factorA', models.DecimalField(db_column='AccRateDOEFactorA', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_DOE_factorB', models.DecimalField(db_column='AccRateDOEFactorB', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_elevator', models.BooleanField(db_column='AccRateElevator', default=False)),
                ('acc_rate_exclude_legs', models.BooleanField(db_column='AccRateExcludeLegs', default=False)),
                ('acc_rate_extra_stop_rates', models.TextField(db_column='AccRateExtraStopRates', default=None, max_length=4000, null=True)),
                ('acc_rate_increment', models.DecimalField(db_column='AccRateIncrement', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_fuel_price_average', models.TextField(db_column='AccRateFuelPriceAverage', default=None, max_length=10, null=True)),
                ('acc_rate_max_charge', models.DecimalField(db_column='AccRateMaxCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_min_charge', models.DecimalField(db_column='AccRateMinCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_percent', models.DecimalField(db_column='AccRatePercent', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_field_version1_id', models.BigIntegerField(db_column='AccRateRangeFieldVersion1ID', default=None, null=True)),
                ('acc_rate_range_field_version2_id', models.BigIntegerField(db_column='AccRateRangeFieldVersion2ID', default=None, null=True)),
                ('acc_rate_range_from1', models.DecimalField(db_column='AccRateRangeFrom1', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_to1', models.DecimalField(db_column='AccRateRangeTo1', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_from2', models.DecimalField(db_column='AccRateRangeFrom2', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_range_to2', models.DecimalField(db_column='AccRateRangeTo2', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_shipping_instructionID', models.BigIntegerField(db_column='AccRateShippingInstructionID', default=None, null=True)),
                ('acc_rate_survey', models.BooleanField(db_column='AccRateSurvey', default=False)),
                ('acc_rate_stairs', models.BooleanField(db_column='AccRateStairs', default=False)),
                ('acc_rate_status_code', models.TextField(db_column='AccRateStatusCode', default=None, max_length=10, null=True)),
                ('acc_rate_threshold_amount', models.DecimalField(db_column='AccRateThresholdAmount', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_rate_vehicle_restricted', models.BooleanField(db_column='AccRateVehicleRestricted', default=False)),
                ('min_std_charge', models.DecimalField(db_column='MinStdCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_override_id', models.ForeignKey(db_column='AccOverrideID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialOverride')),
                ('commodity_version_id', models.ForeignKey(db_column='CommodityVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.CommodityHistory')),
                ('destination_zone_version_id', models.ForeignKey(db_column='DestinationZoneVersionID', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.ZoneHistory')),
                ('origin_zone_version_id', models.ForeignKey(db_column='OriginZoneVersionID', default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.ZoneHistory')),
            ],
            options={
                'db_table': 'AccessorialOverride_History',
            },
        ),
        migrations.CreateModel(
            name='AccessorialStorageOverride',
            fields=[
                ('acc_storage_override_id', models.BigAutoField(db_column='AccStorageOverrideID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('tm_storage_override_id', models.BigIntegerField(db_column='TMStorageOverrideID', default=None)),
                ('base_rate', models.BooleanField(db_column='BaseRate', default=False)),
                ('bill_option', models.TextField(db_column='BillOption', default=None, max_length=1, null=True)),
                ('dangerous_goods', models.BooleanField(db_column='DangerousGoods', default=False)),
                ('description', models.TextField(db_column='Description', default=None, max_length=40, null=True)),
                ('effective_from', models.DateTimeField(db_column='EffectiveFrom', default=None)),
                ('effective_to', models.DateTimeField(db_column='EffectiveTo', default=None)),
                ('free_days', models.BigIntegerField(db_column='FreeDays', default=None)),
                ('high_value', models.BooleanField(db_column='HighValue', default=False)),
                ('include_delivery_day', models.BooleanField(db_column='IncludeDeliveryDay', default=False)),
                ('include_terminal_service_calendar', models.BooleanField(db_column='IncludeTerminalServiceCalendar', default=False)),
                ('operations_code', models.TextField(db_column='OperationsCode', default=None, max_length=10, null=True)),
                ('rate_amount', models.DecimalField(db_column='RateAmount', decimal_places=6, default=None, max_digits=19, null=True)),
                ('rate_max', models.DecimalField(db_column='RateMax', decimal_places=6, default=None, max_digits=19, null=True)),
                ('rate_min', models.DecimalField(db_column='RateMin', decimal_places=6, default=None, max_digits=19, null=True)),
                ('rate_per', models.DecimalField(db_column='RatePer', decimal_places=6, default=None, max_digits=19, null=True)),
                ('temp_controlled', models.BooleanField(db_column='TempControlled', default=False)),
                ('min_std_charge', models.DecimalField(db_column='MinStdCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_header_id', models.ForeignKey(db_column='AccHeaderID', on_delete=django.db.models.deletion.CASCADE, to='rrf.AccessorialHeader')),
                ('currency_id', models.ForeignKey(db_column='CurrencyID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Currency')),
            ],
            options={
                'db_table': 'AccessorialStorageOverride',
            },
        ),
        migrations.CreateModel(
            name='AccessorialStorageOverrideHistory',
            fields=[
                ('version_num', models.IntegerField(db_column='VersionNum', default=None)),
                ('is_latest_version', models.BooleanField(db_column='IsLatestVersion', default=False)),
                ('updated_on', models.DateTimeField(db_column='UpdatedOn', default=None)),
                ('updated_by', models.TextField(db_column='UpdatedBy', default=None)),
                ('base_version', models.IntegerField(db_column='BaseVersion', default=None)),
                ('comments', models.TextField(db_column='Comments', default=None)),
                ('is_active', models.BooleanField(db_column='IsActive', default=False)),
                ('is_inactive_viewable', models.BooleanField(db_column='IsInactiveViewable', default=False)),
                ('acc_storage_override_version_id', models.BigAutoField(db_column='AccStorageOverrideVersionID', primary_key=True, serialize=False)),
                ('tm_storage_override_id', models.BigIntegerField(db_column='TMStorageOverrideID', default=None)),
                ('base_rate', models.BooleanField(db_column='BaseRate', default=False)),
                ('bill_option', models.TextField(db_column='BillOption', default=None, max_length=1, null=True)),
                ('dangerous_goods', models.BooleanField(db_column='DangerousGoods', default=False)),
                ('description', models.TextField(db_column='Description', default=None, max_length=40, null=True)),
                ('effective_from', models.DateTimeField(db_column='EffectiveFrom', default=None)),
                ('effective_to', models.DateTimeField(db_column='EffectiveTo', default=None)),
                ('free_days', models.BigIntegerField(db_column='FreeDays', default=None)),
                ('high_value', models.BooleanField(db_column='HighValue', default=False)),
                ('include_delivery_day', models.BooleanField(db_column='IncludeDeliveryDay', default=False)),
                ('include_terminal_service_calendar', models.BooleanField(db_column='IncludeTerminalServiceCalendar', default=False)),
                ('operations_code', models.TextField(db_column='OperationsCode', default=None, max_length=10, null=True)),
                ('rate_amount', models.DecimalField(db_column='RateAmount', decimal_places=6, default=None, max_digits=19, null=True)),
                ('rate_max', models.DecimalField(db_column='RateMax', decimal_places=6, default=None, max_digits=19, null=True)),
                ('rate_min', models.DecimalField(db_column='RateMin', decimal_places=6, default=None, max_digits=19, null=True)),
                ('rate_per', models.DecimalField(db_column='RatePer', decimal_places=6, default=None, max_digits=19, null=True)),
                ('temp_controlled', models.BooleanField(db_column='TempControlled', default=False)),
                ('min_std_charge', models.DecimalField(db_column='MinStdCharge', decimal_places=6, default=None, max_digits=19, null=True)),
                ('acc_header_version_id', models.ForeignKey(db_column='AccHeaderVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccessorialHeaderHistory')),
                ('acc_storage_override_id', models.ForeignKey(db_column='AccStorageOverrideID', on_delete=django.db.models.deletion.CASCADE, to='rrf.AccessorialStorage')),
                ('currency_version_id', models.ForeignKey(db_column='CurrencyVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.CurrencyHistory')),
            ],
            options={
                'db_table': 'AccessorialStorageOverride_History',
            },
        ),
        migrations.AddField(
            model_name='request',
            name='request_source_id',
            field=models.BigIntegerField(db_column='RequestSourceID', null=True),
        ),
        migrations.AddField(
            model_name='requesthistory',
            name='request_source_id',
            field=models.ForeignKey(db_column='RequestSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='requestsectionlane',
            name='request_section_lane_source_id',
            field=models.BigIntegerField(db_column='RequestSectionLaneSourceID', null=True),
        ),
        migrations.AddField(
            model_name='requestsectionlanehistory',
            name='request_section_lane_source_id',
            field=models.ForeignKey(db_column='RequestSectionLaneSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestSectionLane'),
        ),
        migrations.AddField(
            model_name='requestsectionlanepricingpoint',
            name='request_section_lane_pricing_point_source_id',
            field=models.BigIntegerField(db_column='RequestSectionLanePricingPointSourceID', null=True),
        ),
        migrations.AddField(
            model_name='requestsectionlanepricingpointhistory',
            name='request_section_lane_pricing_point_source_id',
            field=models.ForeignKey(db_column='RequestSectionLanePricingPointSourceID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.RequestSectionLanePricingPoint'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverridehistory',
            name='request_version_id',
            field=models.ForeignKey(db_column='RequestVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverridehistory',
            name='sub_service_level_version_id',
            field=models.ForeignKey(db_column='SubServiceLevelVersionID', on_delete=django.db.models.deletion.CASCADE, to='pac.SubServiceLevelHistory'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverridehistory',
            name='unit_version_id',
            field=models.ForeignKey(db_column='UnitVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.UnitHistory'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverride',
            name='request_id',
            field=models.ForeignKey(db_column='RequestID', on_delete=django.db.models.deletion.CASCADE, to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverride',
            name='sub_service_level_id',
            field=models.ForeignKey(db_column='SubServiceLevelID', on_delete=django.db.models.deletion.CASCADE, to='pac.SubServiceLevel'),
        ),
        migrations.AddField(
            model_name='accessorialstorageoverride',
            name='unit_id',
            field=models.ForeignKey(db_column='UnitID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.Unit'),
        ),
        migrations.AddField(
            model_name='accessorialoverridehistory',
            name='request_version_id',
            field=models.ForeignKey(db_column='RequestID', on_delete=django.db.models.deletion.CASCADE, to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialoverridehistory',
            name='sub_service_level_version_id',
            field=models.ForeignKey(db_column='SubServiceLevelVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.SubServiceLevelHistory'),
        ),
        migrations.AddField(
            model_name='accessorialoverride',
            name='request_id',
            field=models.ForeignKey(db_column='RequestID', on_delete=django.db.models.deletion.CASCADE, to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialoverride',
            name='sub_service_level_id',
            field=models.ForeignKey(db_column='SubServiceLevelID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.SubServiceLevel'),
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverridehistory',
            name='request_version_id',
            field=models.ForeignKey(db_column='RequestVersionID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverridehistory',
            name='sub_service_level_version_id',
            field=models.ForeignKey(db_column='SubServiceLevelVersionID', on_delete=django.db.models.deletion.CASCADE, to='pac.SubServiceLevelHistory'),
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverride',
            name='request_id',
            field=models.ForeignKey(db_column='RequestID', on_delete=django.db.models.deletion.CASCADE, to='rrf.Request'),
        ),
        migrations.AddField(
            model_name='accessorialdetentionoverride',
            name='sub_service_level_id',
            field=models.ForeignKey(db_column='SubServiceLevelID', on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.SubServiceLevel'),
        ),
        migrations.AlterIndexTogether(
            name='accessorialstorageoverridehistory',
            index_together={('acc_storage_override_id', 'version_num')},
        ),
        migrations.AlterIndexTogether(
            name='accessorialoverridehistory',
            index_together={('acc_override_id', 'version_num')},
        ),
        migrations.AlterIndexTogether(
            name='accessorialdetentionoverridehistory',
            index_together={('acc_detention_override_id', 'version_num')},
        ),
    ]
