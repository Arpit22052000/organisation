# Generated by Django 5.0 on 2024-01-24 11:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0019_customuser_pet_name"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="customuser",
            name="pet_name",
        ),
    ]
