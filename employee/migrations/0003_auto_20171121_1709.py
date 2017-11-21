# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20171121_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.IntegerField(default=1, verbose_name=b'Stats ', choices=[(0, 'Inactive'), (1, 'Active')]),
        ),
    ]
