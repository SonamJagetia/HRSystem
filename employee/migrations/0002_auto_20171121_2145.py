# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import employee.models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='address',
            name='employee',
        ),
        migrations.RemoveField(
            model_name='job',
            name='employee',
        ),
        migrations.AlterField(
            model_name='course',
            name='end_date',
            field=models.DateField(verbose_name=b'Date end'),
        ),
        migrations.AlterField(
            model_name='course',
            name='start_date',
            field=models.DateField(verbose_name=b'Date start'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_date',
            field=models.DateField(verbose_name=b'Date end'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_date',
            field=models.DateField(verbose_name=b'Date start'),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='email_address',
            field=models.EmailField(unique=True, max_length=255, verbose_name=b'Email '),
        ),
        migrations.AlterField(
            model_name='emailaddress',
            name='email_type',
            field=models.CharField(max_length=255, null=True, verbose_name=b'Email Type', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='avatar',
            field=models.ImageField(upload_to=employee.models.avatar_upload_to, verbose_name=b'Photo', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_birth',
            field=models.DateField(null=True, verbose_name=b'Date of Birth ', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='date_of_joining',
            field=models.DateField(null=True, verbose_name=b'Date of join ', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='national_id_number',
            field=models.CharField(max_length=25, verbose_name=b'National ID Number', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='region',
            field=models.CharField(max_length=255, verbose_name=b'Regain', blank=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='status',
            field=models.IntegerField(default=1, max_length=255, verbose_name=b'Stats ', choices=[(0, 'Inactive'), (1, 'Active')]),
        ),
        migrations.DeleteModel(
            name='Address',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]
