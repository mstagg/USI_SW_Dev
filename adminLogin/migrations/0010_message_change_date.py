# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('adminLogin', '0009_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='change_date',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 9, 3, 1, 57, 531000, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
