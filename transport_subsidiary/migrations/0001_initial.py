# Generated by Django 5.0.6 on 2024-06-18 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="UnitName",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "處理單位名稱警局層",
                    models.CharField(blank=True, max_length=10, null=True),
                ),
            ],
            options={
                "verbose_name": "處理單位名稱警局層",
                "verbose_name_plural": "處理單位名稱警局層",
                "db_table": "unit_name",
                "db_table_comment": "處理單位名稱警局層表",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="VehicleType",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "當事者區分_類別_大類別名稱_車種",
                    models.CharField(blank=True, max_length=15, null=True),
                ),
            ],
            options={
                "verbose_name": "當事者區分_類別_大類別名稱_車種",
                "verbose_name_plural": "當事者區分_類別_大類別名稱_車種",
                "db_table": "vehicle_type",
                "db_table_comment": "當事者區分_類別_大類別名稱_車種表",
                "managed": False,
            },
        ),
    ]
