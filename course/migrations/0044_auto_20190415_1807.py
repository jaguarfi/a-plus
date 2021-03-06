# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2019-04-15 15:07
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0043_auto_20190412_1706'),
    ]

    operations = [
        migrations.AlterField(
            model_name='learningobjectcategory',
            name='accept_unofficial_submits',
            field=models.BooleanField(default=False, help_text='Grade unofficial submissions after deadlines have passed or submission limits have been exceeded. The points are stored but not included in official records.'),
        ),
    ]
