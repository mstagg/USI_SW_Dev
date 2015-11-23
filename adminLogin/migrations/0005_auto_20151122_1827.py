# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminLogin', '0004_auto_20151118_1314'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountStatus',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('security_code', models.CharField(max_length=8)),
                ('active_code', models.BooleanField(default=True)),
                ('token_amount', models.IntegerField()),
                ('change_date', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='TokenHistory',
        ),
    ]
