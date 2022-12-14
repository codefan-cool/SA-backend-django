# Generated by Django 2.1.13 on 2022-06-30 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rrf', '0092_auto_20220623_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessorialdetail',
            name='acc_rate_factor_id',
            field=models.ForeignKey(blank=True, db_column='AccRateFactorID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.AccFactor'),
        ),
        migrations.AlterField(
            model_name='accessorialdetail',
            name='commodity_id',
            field=models.ForeignKey(blank=True, db_column='CommodityID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='rrf.Commodity'),
        ),
        migrations.AlterField(
            model_name='accessorialdetail',
            name='sub_service_level_id',
            field=models.ForeignKey(blank=True, db_column='SubServiceLevelID', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='pac.SubServiceLevel'),
        ),
    ]
