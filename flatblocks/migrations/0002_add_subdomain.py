# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatblocks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flatblock',
            name='subdomain',
            field=models.CharField(verbose_name='Subdomain', max_length=255, blank=True,
                                   help_text='A subdomain under which the content will be displayed'),
            preserve_default=False,
        ),
    ]
