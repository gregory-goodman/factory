# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-15 10:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0002_auto_20160915_0957'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='file',
            field=models.FileField(upload_to='media/files/', verbose_name='Файл'),
        ),
    ]