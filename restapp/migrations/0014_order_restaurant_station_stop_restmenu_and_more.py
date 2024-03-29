# Generated by Django 4.1.7 on 2023-02-21 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0013_remove_expert_service_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
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
                ("order_id", models.CharField(max_length=6)),
                ("order_date", models.DateField(null=True)),
                ("delivery_date", models.DateField(null=True)),
                ("user_id", models.CharField(max_length=6)),
                ("contact_no", models.CharField(max_length=10)),
                ("coach_no", models.CharField(max_length=4)),
                ("seat_no", models.IntegerField(default=0)),
                (
                    "order_status",
                    models.CharField(
                        choices=[
                            ("0", "Initial"),
                            ("1", "Payment Done"),
                            ("2", "Payment Failed"),
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
                ("item_count", models.IntegerField(default=0)),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("total_discount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("tax", models.DecimalField(decimal_places=2, max_digits=6)),
                ("net_amount", models.DecimalField(decimal_places=2, max_digits=6)),
            ],
            options={"ordering": ["order_id"],},
        ),
        migrations.CreateModel(
            name="Restaurant",
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
                ("rest_id", models.CharField(max_length=6)),
                (
                    "rest_name",
                    models.CharField(help_text="Restaurant Name", max_length=40),
                ),
                ("rest_address", models.CharField(max_length=120)),
                ("contact_person", models.CharField(max_length=40)),
                ("contact_no", models.CharField(max_length=10)),
                ("rest_rating", models.IntegerField(default=0)),
                (
                    "rest_status",
                    models.CharField(
                        choices=[("1", "Open"), ("0", "Closed")],
                        default="1",
                        max_length=1,
                    ),
                ),
            ],
            options={"ordering": ["rest_name"],},
        ),
        migrations.CreateModel(
            name="Station",
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
                ("station_code", models.CharField(max_length=5)),
                ("station_name", models.CharField(max_length=40)),
            ],
            options={"ordering": ["station_code"],},
        ),
        migrations.CreateModel(
            name="Stop",
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
                ("stop_no", models.IntegerField(default=0)),
                ("arrival_time", models.CharField(max_length=5)),
                ("departure_time", models.CharField(max_length=5)),
                ("halt", models.CharField(max_length=4)),
                ("day", models.CharField(max_length=4)),
                (
                    "station_code",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restapp.station",
                    ),
                ),
                (
                    "train_no",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restapp.train",
                    ),
                ),
            ],
            options={"ordering": ["train_no", "stop_no"],},
        ),
        migrations.CreateModel(
            name="RestMenu",
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
                ("menu_id", models.CharField(max_length=6)),
                ("item_name", models.CharField(max_length=40)),
                ("item_desc", models.CharField(max_length=120)),
                ("item_type", models.CharField(max_length=10)),
                ("item_rate", models.DecimalField(decimal_places=2, max_digits=6)),
                ("item_discount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("item_rating", models.IntegerField(default=0)),
                (
                    "item_status",
                    models.CharField(
                        choices=[("1", "Available"), ("0", "Unavailable")],
                        default="1",
                        max_length=1,
                    ),
                ),
                (
                    "rest_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restapp.restaurant",
                    ),
                ),
            ],
            options={"ordering": ["item_name"],},
        ),
        migrations.AddField(
            model_name="restaurant",
            name="rest_location_code",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="restapp.station",
            ),
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("payment_id", models.CharField(max_length=6)),
                ("payment_date", models.DateField(null=True)),
                ("payment_amount", models.DecimalField(decimal_places=2, max_digits=6)),
                ("payment_mode", models.CharField(max_length=10)),
                ("payment_ref", models.CharField(max_length=20)),
                (
                    "payment_status",
                    models.CharField(
                        choices=[("1", "Success"), ("0", "Failed")],
                        default="0",
                        max_length=1,
                    ),
                ),
                (
                    "order_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restapp.order",
                    ),
                ),
            ],
            options={"ordering": ["payment_id"],},
        ),
        migrations.CreateModel(
            name="OrderItem",
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
                ("item_id", models.CharField(max_length=6)),
                ("item_name", models.CharField(max_length=40)),
                ("item_quantity", models.IntegerField(default=0)),
                ("item_rate", models.DecimalField(decimal_places=2, max_digits=6)),
                ("item_discount", models.DecimalField(decimal_places=2, max_digits=6)),
                (
                    "order_id",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="restapp.order",
                    ),
                ),
            ],
            options={"ordering": ["item_id"],},
        ),
        migrations.AddField(
            model_name="order",
            name="rest_id",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="restapp.restaurant",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="station_code",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="restapp.station",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="train_no",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="restapp.train",
            ),
        ),
    ]
