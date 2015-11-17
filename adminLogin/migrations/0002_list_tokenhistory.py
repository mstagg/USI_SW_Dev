# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminLogin', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('size', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TokenHistory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('prev_amount', models.IntegerField()),
                ('new_amount', models.IntegerField()),
                ('change_amount', models.IntegerField()),
                ('change_datetime', models.DateTimeField()),
                ('current_amount', models.IntegerField()),
            ],
        ),
    ]
