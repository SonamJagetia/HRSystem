# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields
import employee.models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('street1', models.CharField(max_length=255, blank=True)),
                ('street2', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('region', models.CharField(max_length=255, blank=True)),
                ('country', models.CharField(max_length=255, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactDetails',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', models.CharField(max_length=25, blank=True)),
                ('phone_type', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('course_name', models.CharField(max_length=50)),
                ('school_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('grade', models.CharField(max_length=50)),
                ('school_city', models.CharField(max_length=50)),
                ('school_country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('education_level', models.CharField(max_length=50)),
                ('major', models.CharField(max_length=50)),
                ('school_name', models.CharField(max_length=100)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('grade', models.CharField(max_length=50)),
                ('school_city', models.CharField(max_length=50)),
                ('school_country', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('email_address', models.EmailField(unique=True, max_length=255)),
                ('email_type', models.CharField(max_length=255, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, verbose_name='created', editable=False)),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, verbose_name='modified', editable=False)),
                ('first_name', models.CharField(max_length=50, blank=True)),
                ('middle_name', models.CharField(max_length=50, blank=True)),
                ('last_name', models.CharField(max_length=50, blank=True)),
                ('gender', models.CharField(default=b'm', max_length=1, choices=[(b'm', 'Male'), (b'f', 'Female')])),
                ('date_of_birth', models.DateField(null=True, blank=True)),
                ('national_id_number', models.CharField(max_length=25, blank=True)),
                ('avatar', models.ImageField(upload_to=employee.models.avatar_upload_to, blank=True)),
                ('street1', models.CharField(max_length=255, blank=True)),
                ('street2', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('region', models.CharField(max_length=255, blank=True)),
                ('country', models.CharField(max_length=255, blank=True)),
                ('job_title', models.CharField(max_length=255, blank=True)),
                ('department', models.CharField(max_length=255, blank=True)),
                ('office_number', models.CharField(max_length=25, blank=True)),
                ('salary', models.IntegerField(blank=True)),
                ('date_of_joining', models.DateField(null=True, blank=True)),
                ('status', models.CharField(default=1, max_length=255, choices=[(0, 'Inactive'), (1, 'Active')])),
                ('manager', models.CharField(max_length=255, blank=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, blank=True)),
                ('department', models.CharField(max_length=255, blank=True)),
                ('city', models.CharField(max_length=255, blank=True)),
                ('region', models.CharField(max_length=255, blank=True)),
                ('country', models.CharField(max_length=255, blank=True)),
                ('employee', models.ForeignKey(to='employee.Employee')),
            ],
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='employee',
            field=models.ForeignKey(to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='education',
            name='employee',
            field=models.ForeignKey(to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='course',
            name='employee',
            field=models.ForeignKey(to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='contactdetails',
            name='employee',
            field=models.ForeignKey(to='employee.Employee'),
        ),
        migrations.AddField(
            model_name='address',
            name='employee',
            field=models.ForeignKey(to='employee.Employee'),
        ),
    ]
