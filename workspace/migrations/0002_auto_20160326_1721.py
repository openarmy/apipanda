# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 17:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisation',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='organisations'),
        ),
    ]
