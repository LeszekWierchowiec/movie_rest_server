# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-01-16 11:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mrs', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
