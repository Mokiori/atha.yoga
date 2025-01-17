# Generated by Django 4.1.5 on 2023-02-08 08:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("courses", "0003_coursequestion_courseanswer"),
    ]

    operations = [
        migrations.AddField(
            model_name="basecourse",
            name="lesson_participants_limit",
            field=models.IntegerField(
                blank=True,
                default=100,
                null=True,
                validators=[django.core.validators.MinValueValidator(limit_value=1)],
                verbose_name="Лимит количества участников онлайн-урока",
            ),
        ),
    ]
