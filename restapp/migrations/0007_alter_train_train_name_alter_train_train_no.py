# Generated by Django 4.1.7 on 2023-02-21 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0006_remove_orderitem_order_id_remove_payment_order_id_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="train",
            name="train_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="train", name="train_no", field=models.CharField(max_length=8),
        ),
    ]
