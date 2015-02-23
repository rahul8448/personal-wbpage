# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=50)),
                ('phone_num', models.CharField(max_length=15, null=True, blank=True)),
                ('email', models.EmailField(max_length=75)),
                ('company', models.CharField(max_length=50, null=True, blank=True)),
                ('message', models.CharField(max_length=200, null=True, blank=True)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
