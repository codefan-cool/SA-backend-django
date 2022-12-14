# Generated by Django 2.1.13 on 2022-05-10 19:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pre_costing', '0021_auto_20220426_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='brokercontractcost',
            options={'verbose_name_plural': 'BrokerContractCost'},
        ),
        migrations.AlterModelOptions(
            name='brokercontractcosthistory',
            options={'verbose_name_plural': 'BrokerContractCost_History'},
        ),
        migrations.AlterModelOptions(
            name='currencyexchange',
            options={'verbose_name_plural': 'CurrencyExchange'},
        ),
        migrations.AlterModelOptions(
            name='currencyexchangehistory',
            options={'verbose_name_plural': 'CurrencyExchange_History'},
        ),
        migrations.AlterModelOptions(
            name='dockroute',
            options={'verbose_name_plural': 'DockRoute'},
        ),
        migrations.AlterModelOptions(
            name='dockroutehistory',
            options={'verbose_name_plural': 'DockRoute_History'},
        ),
        migrations.AlterModelOptions(
            name='grireview',
            options={'verbose_name_plural': 'GriReview'},
        ),
        migrations.AlterModelOptions(
            name='grireviewhistory',
            options={'verbose_name_plural': 'GriReview_History'},
        ),
        migrations.AlterModelOptions(
            name='lane',
            options={'verbose_name_plural': 'Lane'},
        ),
        migrations.AlterModelOptions(
            name='lanecost',
            options={'verbose_name_plural': 'LaneCost'},
        ),
        migrations.AlterModelOptions(
            name='lanecosthistory',
            options={'verbose_name_plural': 'LaneCost_History'},
        ),
        migrations.AlterModelOptions(
            name='lanecostweightbreaklevel',
            options={'verbose_name_plural': 'LaneCostWeightBreakLevel'},
        ),
        migrations.AlterModelOptions(
            name='lanecostweightbreaklevelhistory',
            options={'verbose_name_plural': 'LaneCostWeightBreakLevel_History'},
        ),
        migrations.AlterModelOptions(
            name='lanehistory',
            options={'verbose_name_plural': 'Lane_History'},
        ),
        migrations.AlterModelOptions(
            name='laneroute',
            options={'verbose_name_plural': 'LaneRoute'},
        ),
        migrations.AlterModelOptions(
            name='laneroutehistory',
            options={'verbose_name_plural': 'LaneRoute_History'},
        ),
        migrations.AlterModelOptions(
            name='legcost',
            options={'verbose_name_plural': 'LegCost'},
        ),
        migrations.AlterModelOptions(
            name='legcosthistory',
            options={'verbose_name_plural': 'LegCost_History'},
        ),
        migrations.AlterModelOptions(
            name='requestlog',
            options={'verbose_name_plural': 'RequestLog'},
        ),
        migrations.AlterModelOptions(
            name='speedsheet',
            options={'verbose_name_plural': 'SpeedSheet'},
        ),
        migrations.AlterModelOptions(
            name='speedsheethistory',
            options={'verbose_name_plural': 'SpeedSheet_History'},
        ),
        migrations.AlterModelOptions(
            name='spotquotemargin',
            options={'verbose_name_plural': 'SpotQuoteMargin'},
        ),
        migrations.AlterModelOptions(
            name='spotquotemarginhistory',
            options={'verbose_name_plural': 'SpotQuoteMargin_History'},
        ),
        migrations.AlterModelOptions(
            name='terminalcost',
            options={'verbose_name_plural': 'TerminalCost'},
        ),
        migrations.AlterModelOptions(
            name='terminalcosthistory',
            options={'verbose_name_plural': 'TerminalCost_History'},
        ),
        migrations.AlterModelOptions(
            name='terminalcostweightbreaklevel',
            options={'verbose_name_plural': 'TerminalCostWeightBreakLevel'},
        ),
        migrations.AlterModelOptions(
            name='terminalcostweightbreaklevelhistory',
            options={'verbose_name_plural': 'TerminalCostWeightBreakLevel_History'},
        ),
        migrations.AlterModelOptions(
            name='terminalservicepoint',
            options={'verbose_name_plural': 'TerminalServicePoint'},
        ),
        migrations.AlterModelOptions(
            name='terminalservicepointhistory',
            options={'verbose_name_plural': 'TerminalServicePoint_History'},
        ),
        migrations.AlterModelOptions(
            name='unitconversion',
            options={'verbose_name_plural': 'UnitConversion'},
        ),
        migrations.AlterModelOptions(
            name='unitconversionhistory',
            options={'verbose_name_plural': 'UnitConversion_History'},
        ),
        migrations.AlterIndexTogether(
            name='grireviewhistory',
            index_together={('gri_review', 'version_num')},
        ),
    ]
