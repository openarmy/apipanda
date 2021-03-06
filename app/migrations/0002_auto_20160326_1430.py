# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-03-26 14:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workspace', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subdomain', to='workspace.Organisation'),
        ),
        migrations.AddField(
            model_name='billing',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='billing',
            name='organisation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bills', to='workspace.Organisation'),
        ),
        migrations.AlterUniqueTogether(
            name='client',
            unique_together=set([('name', 'organisation')]),
        ),
        migrations.AlterUniqueTogether(
            name='billing',
            unique_together=set([('reference', 'authorization_code')]),
        ),
    ]
