# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website_frontend', '0003_checked_out_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checked_out',
            name='email',
        ),
    ]
