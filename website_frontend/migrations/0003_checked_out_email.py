# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_frontend', '0002_books_checked_out_library_cards'),
    ]

    operations = [
        migrations.AddField(
            model_name='checked_out',
            name='email',
            field=models.CharField(max_length=50, default='to be made'),
        ),
    ]
