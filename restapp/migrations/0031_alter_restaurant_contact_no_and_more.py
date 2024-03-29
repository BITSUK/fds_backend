# Generated by Django 4.1.7 on 2023-02-24 14:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0030_alter_stop_arrival_time_alter_stop_departure_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="restaurant",
            name="contact_no",
            field=models.CharField(default="-", max_length=10),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="contact_person",
            field=models.CharField(default="-", max_length=40),
        ),
        migrations.AlterField(
            model_name="restaurant",
            name="user_id",
            field=models.CharField(default="-", max_length=6),
        ),
        migrations.AlterField(
            model_name="stop",
            name="arrival_time",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stop",
            name="departure_time",
            field=models.CharField(default=1, max_length=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="stop",
            name="halt",
            field=models.CharField(default=1, max_length=4),
            preserve_default=False,
        ),
    ]
