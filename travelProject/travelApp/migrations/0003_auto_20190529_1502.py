# Generated by Django 2.0.6 on 2019-05-29 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0002_locationlog_date_of_visit'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationlog',
            name='location_lat',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='locationlog',
            name='location_long',
            field=models.IntegerField(default=0),
        ),
    ]
