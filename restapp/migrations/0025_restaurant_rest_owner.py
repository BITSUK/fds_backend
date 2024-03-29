# Generated by Django 4.1.7 on 2023-02-24 05:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("restapp", "0024_alter_appuser_user_role"),
    ]

    operations = [
        migrations.AddField(
            model_name="restaurant",
            name="rest_owner",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="rests",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
