# Generated by Django 2.2.3 on 2019-07-14 12:53

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0014_auto_20190712_1621'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 14, 12, 53, 58, 514014, tzinfo=utc)),
        ),
    ]