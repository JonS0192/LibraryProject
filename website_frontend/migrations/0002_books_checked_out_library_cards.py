# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_frontend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('isbn', models.CharField(primary_key=True, max_length=7, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='library_cards',
            fields=[
                ('id', models.CharField(primary_key=True, max_length=7, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='checked_out',
            fields=[
                ('isbn', models.ForeignKey(primary_key=True, to='website_frontend.books', serialize=False)),
                ('checked_out_date', models.DateField()),
                ('id', models.ForeignKey(to='website_frontend.library_cards')),
            ],
        ),
    ]
