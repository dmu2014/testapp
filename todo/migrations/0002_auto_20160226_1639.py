# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 16:39
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='list',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='list',
            name='group',
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date',)},
        ),
        migrations.RemoveField(
            model_name='comment',
            name='body',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='task',
        ),
        migrations.RemoveField(
            model_name='item',
            name='completed',
        ),
        migrations.RemoveField(
            model_name='item',
            name='list',
        ),
        migrations.RemoveField(
            model_name='item',
            name='project_Id',
        ),
        migrations.RemoveField(
            model_name='item',
            name='status',
        ),
        migrations.RemoveField(
            model_name='item',
            name='time_allocated',
        ),
        migrations.AddField(
            model_name='comment',
            name='item',
            field=models.ForeignKey(default='99', on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='todo.Item'),
        ),
        migrations.AddField(
            model_name='comment',
            name='red_flag',
            field=models.BooleanField(default=None),
        ),
        migrations.AddField(
            model_name='comment',
            name='text',
            field=models.TextField(default='Add updates here'),
        ),
        migrations.AddField(
            model_name='item',
            name='Project_Id',
            field=models.CharField(choices=[('wcc-sw-nfa', 'wcc-sw-nfa'), ('wcc-sw-wiced-stack', 'wcc-sw-wiced-stack')], default='Add Project ID here', max_length=140),
        ),
        migrations.AddField(
            model_name='item',
            name='State',
            field=models.CharField(choices=[('New', 'New'), ('In Progress', 'In Progress'), ('Complete', 'Complete')], default='New', max_length=16),
        ),
        migrations.AlterField(
            model_name='comment',
            name='author',
            field=models.CharField(default='Add Author', max_length=40),
        ),
        migrations.AlterField(
            model_name='item',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todo_created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='item',
            name='note',
            field=models.TextField(max_length=400, null=True),
        ),
        migrations.AlterField(
            model_name='item',
            name='priority',
            field=models.CharField(choices=[('Low', 'Low'), ('Normal', 'Normal'), ('High', 'High')], default='Normal', max_length=6),
        ),
        migrations.AlterField(
            model_name='item',
            name='subcategory_Id',
            field=models.CharField(choices=[('NFA11', 'NFA11'), ('NFA20', 'NFA20'), ('NFCA 3.0', 'NFCA 3.0'), ('BTEWICED 2.0', 'BTEWICED 2.0')], default='Add Sub Project ID here', max_length=140),
        ),
        migrations.AlterField(
            model_name='item',
            name='title',
            field=models.CharField(default='Add a Task title here', max_length=140),
        ),
        migrations.DeleteModel(
            name='List',
        ),
    ]
