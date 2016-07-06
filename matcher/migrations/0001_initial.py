# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-06 20:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wealthmap', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LongBeachOpportunity',
            fields=[
                ('opportunity_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wealthmap.Opportunity')),
            ],
            options={
                'abstract': False,
            },
            bases=('wealthmap.opportunity',),
        ),
    ]
