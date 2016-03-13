# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-13 05:02
from __future__ import unicode_literals

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
            name='Api',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('request_host', models.CharField(max_length=255, verbose_name='host')),
                ('strip_request_path', models.BooleanField(default=False)),
                ('preserve_host', models.BooleanField(default=False)),
                ('upstream_url', models.URLField(verbose_name='url')),
                ('active', models.BooleanField(default=True)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Api',
                'verbose_name_plural': 'Apis',
            },
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_path', models.CharField(max_length=255, verbose_name='path')),
                ('active', models.BooleanField(default=True)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='endpoints', to='endpoint.Api')),
            ],
            options={
                'verbose_name': 'Endpoint',
                'verbose_name_plural': 'Endpoints',
            },
        ),
    ]
