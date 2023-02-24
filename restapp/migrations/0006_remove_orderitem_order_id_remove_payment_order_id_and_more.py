# Generated by Django 4.1.7 on 2023-02-21 06:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0005_alter_order_options_alter_orderitem_options_and_more"),
    ]

    operations = [
        migrations.RemoveField(model_name="orderitem", name="order_id",),
        migrations.RemoveField(model_name="payment", name="order_id",),
        migrations.RemoveField(model_name="restaurant", name="rest_location_code",),
        migrations.RemoveField(model_name="restmenu", name="rest_id",),
        migrations.RemoveField(model_name="stop", name="station_code",),
        migrations.RemoveField(model_name="stop", name="train_no",),
        migrations.AlterModelOptions(name="train", options={},),
        migrations.DeleteModel(name="Order",),
        migrations.DeleteModel(name="OrderItem",),
        migrations.DeleteModel(name="Payment",),
        migrations.DeleteModel(name="Restaurant",),
        migrations.DeleteModel(name="RestMenu",),
        migrations.DeleteModel(name="Station",),
        migrations.DeleteModel(name="Stop",),
    ]