# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django_mysql.models import ListCharField


class ActivitiesTable(models.Model):
    activityid = models.AutoField(db_column='activityID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=255, blank=True, null=True)
    notes = models.CharField(max_length=511, blank=True, null=True)
    location = models.CharField(max_length=511, blank=True, null=True)


class DeadlinesTable(models.Model):
    deadlineid = models.AutoField(db_column='deadlineID', primary_key=True)  # Field name made lowercase.
    moduleid = models.IntegerField(db_column='moduleID')  # Field name made lowercase.
    name = models.CharField(max_length=150)
    type = models.CharField(max_length=32, blank=True, null=True)
    date_due = models.DateTimeField(blank=True, null=True)
    summative = models.IntegerField()
    avg_time = models.FloatField(blank=True, null=True)


class EventsTable(models.Model):
    eventid = models.AutoField(db_column='eventID', primary_key=True)  # Field name made lowercase.
    username = models.CharField(max_length=20)  # Field name made lowercase 
    event_type = models.CharField(max_length=10)
    deadlineid = models.SmallIntegerField(db_column='deadlineID', blank=True, null=True)  # Field name made lowercase.
    activityid = models.SmallIntegerField(db_column='activityID', blank=True, null=True)  # Field name made lowercase.
    attendanceid = models.SmallIntegerField(db_column='attendanceID', blank=True, null=True)  # Field name made lowercase.
    time_start = models.DateTimeField(blank=True, null=True)
    time_finish = models.DateTimeField(blank=True, null=True)


class ModulesTable(models.Model):
    moduleid = models.AutoField(db_column='moduleID', primary_key=True)  # Field name made lowercase.
    code = models.CharField(max_length=9)
    title = models.CharField(max_length=128)


class Profile(models.Model):
    username = models.CharField(max_length=20, unique=True, primary_key=True)
    fullname = models.CharField(max_length=150, blank=True, null=True)
    ics_file = models.CharField(max_length=256, blank=True, null=True)
    available_days = ListCharField(base_field=models.CharField(max_length=10), size=7, max_length=(7 * 11), blank=True, null=True)
    available_hours = ListCharField(base_field=models.CharField(max_length=6), size=2, max_length=(2 * 7), blank=True, null=True)
    finish_days_before = models.IntegerField(blank=True, null=True)
    max_sub_deadline_events_per_day = models.IntegerField(blank=True, null=True)
    break_time = models.IntegerField(blank=True, null=True)
    study_session = models.IntegerField(blank=True, null=True)
