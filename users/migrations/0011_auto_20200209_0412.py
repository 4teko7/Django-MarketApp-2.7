# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20200209_0402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(help_text='Telefon Numaras\u0131'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=11, verbose_name='Telefon Numarasi/Phone Number'),
        ),
    ]
