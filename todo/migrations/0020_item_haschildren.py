# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-03-02 20:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0019_auto_20160302_1335'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='haschildren',
            field=models.NullBooleanField(),
        ),
    ]