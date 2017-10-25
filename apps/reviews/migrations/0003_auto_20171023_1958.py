# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-10-23 19:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20171023_1922'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='book_id',
        ),
        migrations.AddField(
            model_name='review',
            name='book_obj',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='book_reviews', to='reviews.Book'),
        ),
        migrations.AlterField(
            model_name='review',
            name='reviewer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reviews', to='reviews.User'),
        ),
    ]
