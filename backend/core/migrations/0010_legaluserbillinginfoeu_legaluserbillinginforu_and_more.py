# Generated by Django 4.1.6 on 2023-02-07 19:20

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("contenttypes", "0002_remove_content_type_name"),
        ("core", "0009_user_region"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userbillinginforu",
            name="userbillinginfo_ptr",
        ),
        migrations.DeleteModel(
            name="UserBillingInfoEU",
        ),
        migrations.DeleteModel(
            name="UserBillingInfoRU",
        ),
        migrations.RenameModel(
            old_name="UserBillingInfo",
            new_name="LegalUserBillingInfo",
        ),
        migrations.CreateModel(
            name="LegalUserBillingInfoEU",
            fields=[
                (
                    "legaluserbillinginfo_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.legaluserbillinginfo",
                    ),
                ),
                ("inn", models.CharField(max_length=50, verbose_name="ИНН")),
                (
                    "correspondent_account",
                    models.CharField(
                        max_length=50, verbose_name="Корреспондентский счет"
                    ),
                ),
                ("prc", models.CharField(max_length=50, verbose_name="КПП")),
                ("bic", models.CharField(max_length=50)),
                (
                    "account_number",
                    models.CharField(max_length=50, verbose_name="Номер счета"),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("core.legaluserbillinginfo",),
        ),
        migrations.CreateModel(
            name="LegalUserBillingInfoRU",
            fields=[
                (
                    "legaluserbillinginfo_ptr",
                    models.OneToOneField(
                        auto_created=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        parent_link=True,
                        primary_key=True,
                        serialize=False,
                        to="core.legaluserbillinginfo",
                    ),
                ),
                (
                    "inn",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(regex="^\\d{10}$")
                        ],
                        verbose_name="ИНН",
                    ),
                ),
                (
                    "correspondent_account",
                    models.CharField(
                        max_length=20,
                        validators=[
                            django.core.validators.RegexValidator(regex="^\\d{20}$")
                        ],
                        verbose_name="Корреспондентский счет",
                    ),
                ),
                (
                    "prc",
                    models.CharField(
                        max_length=10,
                        validators=[
                            django.core.validators.RegexValidator(regex="^\\d{10}$")
                        ],
                        verbose_name="КПП",
                    ),
                ),
                (
                    "bic",
                    models.CharField(
                        max_length=50,
                        validators=[
                            django.core.validators.RegexValidator(regex="^[A-Z0-9]{9}$")
                        ],
                        verbose_name="БИК",
                    ),
                ),
                (
                    "account_number",
                    models.CharField(max_length=30, verbose_name="Номер счета"),
                ),
            ],
            options={
                "abstract": False,
                "base_manager_name": "objects",
            },
            bases=("core.legaluserbillinginfo",),
        ),
    ]
