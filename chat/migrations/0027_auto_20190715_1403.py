# Generated by Django 2.2.3 on 2019-07-15 14:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0026_auto_20190715_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatmessage',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 15, 14, 3, 23, 259056, tzinfo=utc)),
        ),
    ]