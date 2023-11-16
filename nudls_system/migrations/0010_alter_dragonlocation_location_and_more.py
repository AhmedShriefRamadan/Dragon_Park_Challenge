# Generated by Django 4.2.7 on 2023-11-16 11:36

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("nudls_system", "0009_alter_zone_maintainence_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dragonlocation",
            name="location",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="nudls_system.zone"
            ),
        ),
        migrations.AlterField(
            model_name="zone",
            name="maintainence_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 16, 13, 36, 25, 699486)
            ),
        ),
    ]