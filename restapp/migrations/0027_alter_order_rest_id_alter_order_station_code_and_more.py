# Generated by Django 4.1.7 on 2023-02-24 06:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0026_remove_restaurant_rest_owner"),
    ]

    operations = [
        migrations.AlterField(
            model_name="order",
            name="rest_id",
            field=models.CharField(default=99, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="station_code",
            field=models.CharField(default=99, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="order",
            name="train_no",
            field=models.CharField(default=99, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="orderitem",
            name="order_id",
            field=models.CharField(default=99, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="payment",
            name="order_id",
            field=models.CharField(default=99, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="rest_location_code",
            field=models.CharField(default=99, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="restmenu",
            name="rest_id",
            field=models.CharField(default=99, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stop",
            name="station_code",
            field=models.CharField(default=99, max_length=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stop",
            name="train_no",
            field=models.CharField(default=99, max_length=8),
            preserve_default=False,
        ),
    ]