# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 01:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20200209_0424'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.TextField(help_text='Adres'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(default='', max_length=100, verbose_name='Soyad\u0131n\u0131z/Lastname'),
        ),
    ]