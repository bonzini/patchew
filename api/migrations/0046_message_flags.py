# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-18 14:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0045_message_maintainers'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='flags',
            field=models.CharField(blank=True, default='', max_length=64),
        ),
    ]