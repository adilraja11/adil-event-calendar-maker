# Generated by Django 5.1.7 on 2025-04-08 14:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models

import apps.utils


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Event",
            fields=[
                (
                    "id",
                    models.CharField(
                        default=apps.utils.generate_id,
                        editable=False,
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "location",
                    models.CharField(
                        choices=[
                            ("online", "Online"),
                            ("jakarta", "Jakarta"),
                            ("bandung", "Bandung"),
                            ("surabaya", "Surabaya"),
                            ("yogyakarta", "Yogyakarta"),
                            ("bali", "Bali"),
                        ],
                        max_length=20,
                    ),
                ),
                ("description", models.TextField()),
                ("date", models.DateField()),
                (
                    "created_by",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
