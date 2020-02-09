# -*- coding: utf-8 -*-
# Generated by Django 1.11.27 on 2020-02-09 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='address',
            field=models.TextField(default='', help_text='Adres'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='firstName',
            field=models.CharField(default='', max_length=100, verbose_name='Ad\u0131n\u0131z/Name'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='lastName',
            field=models.CharField(default='', max_length=100, verbose_name='Soyad\u0131n\u0131z/Lastname'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(default=0, max_length=11, verbose_name='Telefon Numarasi/Phone Number'),
        ),
    ]