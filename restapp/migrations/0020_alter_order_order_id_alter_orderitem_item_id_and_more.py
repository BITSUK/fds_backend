# Generated by Django 4.1.7 on 2023-02-21 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0019_restaurant_rest_type"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order", name="order_id", field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="item_id",
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name="payment",
            name="payment_id",
            field=models.CharField(max_length=12),
        ),
        migrations.AlterField(
            model_name="restmenu",
            name="menu_id",
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name="station",
            name="station_code",
            field=models.CharField(max_length=8),
        ),
    ]
