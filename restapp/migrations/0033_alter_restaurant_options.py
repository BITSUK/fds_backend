# Generated by Django 4.1.7 on 2023-02-25 04:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0032_rename_user_id_restaurant_rest_owner"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="restaurant", options={"ordering": ["rest_id"]},
        ),
    ]
