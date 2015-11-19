# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminLogin', '0003_auto_20151117_2127'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lists',
            field=models.ManyToManyField(to='adminLogin.List'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pin',
            field=models.IntegerField(),
        ),
    ]
