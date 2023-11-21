# Generated by Django 4.2.6 on 2023-11-21 12:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Pay",
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
                (
                    "payday",
                    models.PositiveSmallIntegerField(verbose_name="дата оплаты"),
                ),
                ("is_paid", models.BooleanField(default=True, verbose_name="оплачено")),
                ("summa", models.PositiveIntegerField(verbose_name="сумма оплаты")),
                (
                    "pay_method",
                    models.CharField(
                        choices=[("cash", "наличные"), ("card", "перевод")],
                        default="cash",
                        max_length=10,
                        verbose_name="способ оплаты",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "платеж",
                "verbose_name_plural": "платежи",
            },
        ),
    ]
