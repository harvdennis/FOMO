# Generated by Django 4.0.3 on 2022-03-30 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FomoApp', '0007_delete_attendancetable_alter_eventstable_userid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventstable',
            name='userid',
            field=models.CharField(max_length=20),
        ),
    ]
