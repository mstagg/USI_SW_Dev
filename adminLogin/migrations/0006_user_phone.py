# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminLogin', '0005_auto_20151122_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='phone',
            field=models.BigIntegerField(default=1234567890),
            preserve_default=False,
        ),
    ]
