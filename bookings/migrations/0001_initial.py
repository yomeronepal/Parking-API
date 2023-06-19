# Generated by Django 4.2.2 on 2023-06-19 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("customer_name", models.CharField(max_length=255)),
                ("license_plate", models.CharField(max_length=255)),
                ("bookinh_plate", models.DateTimeField()),
                ("bay_number", models.IntegerField()),
            ],
        ),
    ]
