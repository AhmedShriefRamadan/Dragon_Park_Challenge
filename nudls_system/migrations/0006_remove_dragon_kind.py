# Generated by Django 4.2.7 on 2023-11-16 10:29

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("nudls_system", "0005_remove_dragonlocation_id_alter_dragonlocation_dragon"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dragon",
            name="kind",
        ),
    ]
