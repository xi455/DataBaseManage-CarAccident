# Generated by Django 5.0.6 on 2024-06-13 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("transport", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="accidentrecords",
            options={
                "managed": True,
                "verbose_name": "事故紀錄",
                "verbose_name_plural": "事故紀錄",
            },
        ),
        migrations.AlterModelOptions(
            name="causeanalysis",
            options={
                "managed": True,
                "verbose_name": "原因分析",
                "verbose_name_plural": "原因分析",
            },
        ),
        migrations.AlterModelOptions(
            name="partyinfo",
            options={
                "managed": True,
                "verbose_name": "肇事人紀錄",
                "verbose_name_plural": "肇事人紀錄",
            },
        ),
        migrations.AlterModelOptions(
            name="roadconditions",
            options={
                "managed": True,
                "verbose_name": "道路狀況",
                "verbose_name_plural": "道路狀況",
            },
        ),
        migrations.AlterModelOptions(
            name="trafficfacilities",
            options={
                "managed": True,
                "verbose_name": "交通設施",
                "verbose_name_plural": "交通設施",
            },
        ),
    ]