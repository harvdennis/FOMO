# Generated by Django 4.0.3 on 2022-03-30 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FomoApp', '0006_delete_attendancetable_alter_profile_available_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventstable',
            name='userid',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
