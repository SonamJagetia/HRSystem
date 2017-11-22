from django.contrib import admin
from .models import Employee, EmailAddress, ContactDetails, Education, Course
from django.contrib.auth.models import User
from django.contrib.auth.models import Group

class EmailAddressInline(admin.StackedInline):
    model = EmailAddress
    fields = ('email_address','email_type')

class ContactDetailsInline(admin.StackedInline):
    model = ContactDetails
    fields = ('phone_number','phone_type')

class CourseInline(admin.StackedInline):
    model = Course
    fields = ('course_name','school_name','start_date','end_date','grade','school_city','school_country')

class EducationInline(admin.StackedInline):
    model = Education
    fields = ('education_level','major','school_name','start_date','end_date','grade','school_city','school_country')
    class meta:
        verbose_name = 'Education'

class Employeeadmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'middle_name', 'last_name')
    search_fields = (
        'id',
        'first_name',
        'middle_name',
        'last_name',
    )
    inlines = [EmailAddressInline,ContactDetailsInline,CourseInline,EducationInline,]

admin.site.register(Employee, Employeeadmin)
admin.site.unregister(User)
admin.site.unregister(Group)