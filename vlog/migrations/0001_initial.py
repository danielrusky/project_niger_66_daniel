# Generated by Django 4.2.5 on 2023-11-11 17:17

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
            name="Record",
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
                ("title", models.CharField(max_length=150, verbose_name="Заголовок")),
                (
                    "slug",
                    models.SlugField(max_length=300, unique=True, verbose_name="URL"),
                ),
                ("content", models.TextField(verbose_name="Содержимое")),
                (
                    "preview",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="images/records/",
                        verbose_name="изображение(превью)",
                    ),
                ),
                (
                    "created",
                    models.DateField(auto_now_add=True, verbose_name="дата создания"),
                ),
                (
                    "sign_of_publication",
                    models.BooleanField(default=True, verbose_name="активный"),
                ),
                ("views", models.IntegerField(default=0, verbose_name="просмотры")),
                (
                    "author",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="автор",
                    ),
                ),
            ],
            options={
                "verbose_name": "Запись",
                "verbose_name_plural": "Записи",
                "get_latest_by": "created",
            },
        ),
    ]
