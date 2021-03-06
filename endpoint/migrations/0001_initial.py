# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 14:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield2.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('request', '__first__'),
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
                ('login_required', models.BooleanField(default=False)),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apis', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'API',
                'verbose_name_plural': 'APIs',
            },
        ),
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_path', models.CharField(max_length=255, verbose_name='path')),
                ('active', models.BooleanField(default=True)),
                ('schema', jsonfield2.fields.JSONField(default=dict)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='apis', to='endpoint.Api')),
            ],
            options={
                'verbose_name': 'Endpoint',
                'verbose_name_plural': 'Endpoints',
            },
        ),
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='request.Request')),
                ('meta', jsonfield2.fields.JSONField(default=dict)),
                ('api', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='endpoint.Api')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to=settings.AUTH_USER_MODEL)),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='endpoint.Endpoint')),
            ],
            bases=('request.request',),
        ),
    ]
