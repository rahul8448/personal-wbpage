# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dashboard_messages',
            name='is_read',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
