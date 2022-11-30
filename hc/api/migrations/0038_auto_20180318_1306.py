# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-03-18 13:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0037_auto_20180127_1215")]

    operations = [
        migrations.AddField(
            model_name="check",
            name="has_confirmation_link",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="ping",
            name="body",
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
    ]
