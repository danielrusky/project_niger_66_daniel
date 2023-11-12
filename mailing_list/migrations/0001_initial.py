# Generated by Django 4.2.5 on 2023-11-11 12:53

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Client",
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
                    "first_name",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="имя"
                    ),
                ),
                (
                    "last_name",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="фамилия"
                    ),
                ),
                (
                    "surname",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="отчество"
                    ),
                ),
                ("email", models.EmailField(max_length=150, verbose_name="почта")),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активный"),
                ),
            ],
            options={
                "verbose_name": "Клиент",
                "verbose_name_plural": "Клиенты",
            },
        ),
        migrations.CreateModel(
            name="MailingList",
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
                    "time",
                    models.TimeField(
                        default=datetime.datetime.now, verbose_name="время"
                    ),
                ),
                (
                    "start",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="начало рассылки"
                    ),
                ),
                (
                    "finish",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="окончание рассылки"
                    ),
                ),
                (
                    "periodicity",
                    models.CharField(
                        choices=[
                            ("разовая", "разовая"),
                            ("ежедневно", "ежедневно"),
                            ("еженедельно", "еженедельно"),
                            ("ежемесячно", "ежемесячно"),
                        ],
                        max_length=150,
                        verbose_name="периодичность",
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("создана", "создана"),
                            ("завершена", "завершена"),
                            ("запущена", "запущена"),
                        ],
                        default="начало рассылки",
                        max_length=100,
                        verbose_name="статус",
                    ),
                ),
            ],
            options={
                "verbose_name": "Рассылка",
                "verbose_name_plural": "Рассылки",
            },
        ),
        migrations.CreateModel(
            name="MailingListMessage",
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
                    "subject",
                    models.CharField(max_length=200, verbose_name="тема письма"),
                ),
                ("body", models.TextField(verbose_name="сообщение")),
                (
                    "created",
                    models.DateTimeField(auto_now_add=True, verbose_name="создано"),
                ),
            ],
            options={
                "verbose_name": "Сообщение",
                "verbose_name_plural": "Сообщения",
            },
        ),
        migrations.CreateModel(
            name="MailingListLogs",
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
                    "send_time",
                    models.DateTimeField(
                        auto_now_add=True, verbose_name="время отправки"
                    ),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("delivered", "доставлено"),
                            ("not_delivered", "не доставлено"),
                        ],
                        verbose_name="статус рассылки",
                    ),
                ),
                (
                    "response",
                    models.TextField(
                        blank=True, null=True, verbose_name="ответ почтового сервера"
                    ),
                ),
                (
                    "sending",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="mailing_list.mailinglist",
                        verbose_name="рассылка",
                    ),
                ),
            ],
            options={
                "verbose_name": "Попытка",
                "verbose_name_plural": "Попытки",
            },
        ),
        migrations.AddField(
            model_name="mailinglist",
            name="message",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="mailing_list.mailinglistmessage",
                verbose_name="сообщение",
            ),
        ),
    ]