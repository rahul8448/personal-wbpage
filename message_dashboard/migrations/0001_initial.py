# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DashBoard_Messages',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_name', models.CharField(max_length=20)),
                ('sender_organization', models.CharField(max_length=30)),
                ('sender_email', models.CharField(max_length=20)),
                ('sender_phone', models.CharField(max_length=30, null=True, blank=True)),
                ('message_subject', models.CharField(max_length=50)),
                ('message_body', models.CharField(max_length=200, null=True, blank=True)),
                ('is_read', models.CharField(default=b'F', max_length=200)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'dashboard_messages',
            },
            bases=(models.Model,),
        ),
    ]
