# Generated by Django 4.0.2 on 2022-03-29 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FomoApp', '0003_delete_attendancetable_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deadlinestable',
            name='name',
            field=models.CharField(max_length=150),
        ),
    ]
