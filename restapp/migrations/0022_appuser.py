# Generated by Django 4.1.7 on 2023-02-23 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("restapp", "0021_alter_stop_day"),
    ]

    operations = [
        migrations.CreateModel(
            name="AppUser",
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
                ("user_id", models.CharField(max_length=6)),
                ("user_name", models.CharField(max_length=40)),
                ("user_email", models.CharField(max_length=40)),
                ("user_password", models.CharField(max_length=40)),
                ("user_role", models.IntegerField(default=1)),
            ],
            options={"ordering": ["user_id"],},
        ),
    ]