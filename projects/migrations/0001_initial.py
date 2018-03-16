# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-15 00:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('complete', models.BooleanField()),
                ('github_url', models.URLField()),
                ('description', models.TextField()),
                ('last_modified', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
