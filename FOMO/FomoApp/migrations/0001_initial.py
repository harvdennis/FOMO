# Generated by Django 3.2.12 on 2022-03-29 18:02

from django.db import migrations, models
import django_mysql.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivitiesTable',
            fields=[
                ('activityid', models.AutoField(db_column='activityID', primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=511, null=True)),
                ('location', models.CharField(blank=True, max_length=511, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='AttendanceTable',
            fields=[
                ('attendanceid', models.SmallAutoField(db_column='attendanceID', primary_key=True, serialize=False)),
                ('moduleid', models.IntegerField(db_column='moduleID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
                ('notes', models.CharField(blank=True, max_length=511, null=True)),
                ('location', models.CharField(blank=True, max_length=511, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='DeadlinesTable',
            fields=[
                ('deadlineid', models.SmallIntegerField(db_column='deadlineID', primary_key=True, serialize=False)),
                ('moduleid', models.IntegerField(db_column='moduleID')),
                ('name', models.CharField(max_length=64)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('date_due', models.DateTimeField(blank=True, null=True)),
                ('summative', models.IntegerField()),
                ('avg_time', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EventsTable',
            fields=[
                ('eventid', models.AutoField(db_column='eventID', primary_key=True, serialize=False)),
                ('userid', models.SmallIntegerField(db_column='userID')),
                ('event_type', models.CharField(max_length=10)),
                ('deadlineid', models.SmallIntegerField(blank=True, db_column='deadlineID', null=True)),
                ('activityid', models.SmallIntegerField(blank=True, db_column='activityID', null=True)),
                ('attendanceid', models.SmallIntegerField(blank=True, db_column='attendanceID', null=True)),
                ('time_start', models.DateTimeField(blank=True, null=True)),
                ('time_finish', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ModulesTable',
            fields=[
                ('moduleid', models.AutoField(db_column='moduleID', primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=9)),
                ('title', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('username', models.CharField(max_length=20, primary_key=True, serialize=False, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('ics_file', models.CharField(blank=True, max_length=256)),
                ('available_days', django_mysql.models.ListCharField(models.CharField(max_length=10), max_length=77, size=7)),
                ('available_hours', django_mysql.models.ListCharField(models.CharField(max_length=6), max_length=49, size=7)),
                ('break_time', models.IntegerField()),
                ('study_session', models.IntegerField()),
            ],
        ),
    ]