# Generated by Django 2.0.6 on 2019-05-29 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travelApp', '0004_auto_20190529_1505'),
    ]

    operations = [
        migrations.AddField(
            model_name='locationrating',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
