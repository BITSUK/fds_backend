# Generated by Django 4.1.7 on 2023-02-21 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0012_train"),
    ]

    operations = [
        migrations.RemoveField(model_name="expert", name="service",),
        migrations.RemoveField(model_name="service_request", name="booked_by",),
        migrations.RemoveField(model_name="service_request", name="service",),
        migrations.RemoveField(model_name="service_request", name="serviced_by",),
        migrations.AlterModelOptions(name="train", options={"ordering": ["train_no"]},),
        migrations.AlterField(
            model_name="train",
            name="train_name",
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name="train", name="train_no", field=models.CharField(max_length=8),
        ),
        migrations.DeleteModel(name="Customer",),
        migrations.DeleteModel(name="Expert",),
        migrations.DeleteModel(name="Service",),
        migrations.DeleteModel(name="Service_Request",),
    ]
