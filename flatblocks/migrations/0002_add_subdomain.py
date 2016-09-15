# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flatblocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flatblock',
            name='slug',
            field=models.CharField(help_text='A unique name used for reference in the templates', max_length=255,
                                   verbose_name='Slug'),
        ),
        migrations.AddField(
            model_name='flatblock',
            name='subdomain',
            field=models.CharField(verbose_name='Subdomain', max_length=255, blank=True, null=True,
                                   help_text='A subdomain under which the content will be displayed'),
            preserve_default=False,
        ),
        migrations.AlterUniqueTogether(
            name='flatblock',
            unique_together=set([('slug', 'subdomain')]),
        ),
    ]
