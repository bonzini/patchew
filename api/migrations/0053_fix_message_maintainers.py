# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations
from django.db.models import Q

import email.utils


def maintainers_join_name_addr(apps, schema_editor):
    Message = apps.get_model("api", "Message")
    for m in Message.objects.exclude(maintainers=[]):
        m.maintainers = [("%s <%s>" % (x[0], x[1])) for x in m.maintainers]
        m.save()


def maintainers_split_name_addr(apps, schema_editor):
    Message = apps.get_model("api", "Message")
    for m in Message.objects.exclude(maintainers=[]):
        m.maintainers = [email.utils.parseaddr(x) for x in m.maintainers]
        m.save()


class Migration(migrations.Migration):
    dependencies = [("api", "0052_auto_20190418_1357")]

    operations = [
        migrations.RunPython(
            maintainers_split_name_addr, reverse_code=maintainers_join_name_addr
        )
    ]
