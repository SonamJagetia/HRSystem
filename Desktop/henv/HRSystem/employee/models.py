import os, datetime
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.urlresolvers import reverse
from model_utils.models import TimeStampedModel
from django.utils.translation import ugettext_lazy as _


GENDER_CHOICES = (
    ("m", _("Male")),
    ("f", _("Female")),
)

STATUS_CHOICES = (
    (0, _("Inactive")),
    (1, _("Active")),
)


def avatar_upload_to(instance, filename):
    # contruct filename base on user_id
    filename = 'avatar/{0}{1}'.format(
        instance.id,
        os.path.splitext(filename.lower())[1]
    )
    return filename


class Employee(TimeStampedModel):
    first_name = models.CharField(max_length=50, blank=True)
    middle_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, default="m")
    date_of_birth = models.DateField(blank=True, null=True,verbose_name='Date of Birth ')
    national_id_number = models.CharField(max_length=25,blank=True, verbose_name='National ID Number')
    avatar = models.ImageField(blank=True, upload_to=avatar_upload_to, verbose_name='Photo')
    street1 = models.CharField(max_length=255, blank=True)
    street2 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=255, blank=True)
    region = models.CharField(max_length=255, blank=True, verbose_name='Regain')
    country = models.CharField(max_length=255, blank=True)
    job_title = models.CharField(max_length=255, blank=True)
    department = models.CharField(max_length=255, blank=True)
    office_number = models.CharField(max_length=25, blank=True)
    salary = models.IntegerField(blank=True)
    date_of_joining = models.DateField(blank=True, null=True, verbose_name='Date of join ')
    status = models.IntegerField(choices=STATUS_CHOICES, default=1, verbose_name='Stats ')
    manager = models.CharField(max_length=255, blank=True)


class EmailAddress(models.Model):
    employee = models.ForeignKey("Employee")
    email_address = models.EmailField(max_length=255, unique=True, verbose_name='Email ')
    email_type = models.CharField(max_length=255, blank=True, null=True, verbose_name='Email Type')


class ContactDetails(models.Model):
    employee = models.ForeignKey("Employee")
    phone_number = models.CharField(max_length=25, blank=True)
    phone_type = models.CharField(max_length=255, blank=True, null=True)


class Education(models.Model):
    employee = models.ForeignKey("Employee")
    education_level = models.CharField(max_length=50)
    major = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    start_date = models.DateField(verbose_name='Date start')
    end_date = models.DateField(verbose_name='Date end')
    grade = models.CharField(max_length=50)
    school_city = models.CharField(max_length=50)
    school_country = models.CharField(max_length=50)

    class meta:
        verbose_name = 'Education'


class Course(models.Model):
    employee = models.ForeignKey("Employee")
    course_name = models.CharField(max_length=50)
    school_name = models.CharField(max_length=100)
    start_date = models.DateField(verbose_name='Date start')
    end_date = models.DateField(verbose_name='Date end')
    grade = models.CharField(max_length=50)
    school_city = models.CharField(max_length=50)
    school_country = models.CharField(max_length=50)
