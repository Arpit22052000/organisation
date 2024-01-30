# Generated by Django 5.0 on 2024-01-15 12:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0006_alter_notes_notes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customuser",
            name="role",
            field=models.IntegerField(
                choices=[(1, "HR"), (2, "Lead"), (3, "Director")], default=1
            ),
        ),
    ]