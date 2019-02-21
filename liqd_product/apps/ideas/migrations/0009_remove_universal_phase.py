# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-24 13:13
from __future__ import unicode_literals

from django.db import migrations


def change_phase(apps, schema_editor):
    Phase = apps.get_model('a4phases', 'Phase')
    for phase in Phase.objects.filter(type='liqd_product_ideas:050:universal'):
        phase.type = 'liqd_product_ideas:050:collect_feedback'
        phase.save()


class Migration(migrations.Migration):

    dependencies = [
        ('liqd_product_ideas', '0008_alter_category'),
    ]

    operations = [
        migrations.RunPython(change_phase),
    ]
