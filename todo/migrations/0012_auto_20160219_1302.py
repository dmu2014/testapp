# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 18:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0011_auto_20160216_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default='Add updates here'),
        ),
        migrations.AlterField(
            model_name='item',
            name='Project_Id',
            field=models.CharField(default='Add Project ID here', max_length=140),
        ),
        migrations.AlterField(
            model_name='item',
            name='State',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], default='New', max_length=16),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory_Id',
            field=models.CharField(default='Add Sub Project ID here', max_length=140),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(default='Add a Task title here', max_length=140),
        ),
    ]
