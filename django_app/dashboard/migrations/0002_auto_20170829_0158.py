# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-29 01:58
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='team',
            name='members',
            field=models.ManyToManyField(related_name='shared_user', through='dashboard.MembersTeams', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membersteams',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='membersteams',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Team'),
        ),
        migrations.AddField(
            model_name='cardlist',
            name='board',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Board'),
        ),
        migrations.AddField(
            model_name='card',
            name='cardlist',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.CardList'),
        ),
        migrations.AddField(
            model_name='board',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='board',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Team'),
        ),
    ]
