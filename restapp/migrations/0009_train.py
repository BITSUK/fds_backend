# Generated by Django 4.1.7 on 2023-02-21 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0008_customer_expert_service_service_request_delete_train_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=10)),
                ('name', models.CharField(help_text='(Train name)', max_length=200)),
            ],
        ),
    ]
