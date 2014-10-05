# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inheritors',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, null=True, blank=True)),
                ('gender', models.CharField(max_length=6, null=True, blank=True)),
                ('alive', models.NullBooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Relationships',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('type', models.CharField(max_length=12)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Testator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('gender', models.CharField(max_length=6)),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='inheritors',
            name='relationType',
            field=models.ForeignKey(blank=True, to='will.Relationships', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inheritors',
            name='relative',
            field=models.ForeignKey(blank=True, to='will.Inheritors', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='inheritors',
            name='testator',
            field=models.ForeignKey(blank=True, to='will.Testator', null=True),
            preserve_default=True,
        ),
    ]
