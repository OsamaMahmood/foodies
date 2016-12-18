# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-18 14:57
from __future__ import unicode_literals

import core.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('phone_number', models.CharField(max_length=15, null=True)),
                ('hours', models.TextField(blank=True, null=True)),
                ('image_file', models.ImageField(blank=True, null=True, upload_to=core.models.upload_to_location)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
