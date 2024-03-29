# Generated by Django 4.1.7 on 2023-02-24 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0027_alter_order_rest_id_alter_order_station_code_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="order_status",
            field=models.CharField(
                choices=[
                    ("0", "Initial"),
                    ("1", "Paid"),
                    ("2", "Pending"),
                    ("3", "Accepted"),
                    ("4", "Rejected"),
                    ("5", "Preparing Food"),
                    ("6", "Order Ready"),
                    ("7", "In Transit"),
                    ("8", "Delivered"),
                    ("9", "Delivery Failed"),
                    ("10", "Cancelled"),
                ],
                default="0",
                max_length=2,
            ),
        ),
    ]
