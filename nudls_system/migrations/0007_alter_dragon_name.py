# Generated by Django 4.2.7 on 2023-11-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("nudls_system", "0006_remove_dragon_kind"),
    ]

    operations = [
        migrations.AlterField(
            model_name="dragon",
            name="name",
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
