# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-26 08:29
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0025_populate_project_maintainers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='prefixes',
            field=jsonfield.fields.JSONField(blank=True),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipients',
            field=jsonfield.fields.JSONField(),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=jsonfield.fields.JSONCharField(db_index=True, max_length=4096),
        ),
    ]
