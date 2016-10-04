# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import djangocms_attributes_field.fields


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0016_auto_20160608_1535'),
    ]

    operations = [
        migrations.CreateModel(
            name='HTMLText',
            fields=[
                ('cmsplugin_ptr', models.OneToOneField(parent_link=True, related_name='djangocms_html_tags_htmltext', auto_created=True, primary_key=True, serialize=False, to='cms.CMSPlugin')),
                ('tag', models.CharField(default=b'div', max_length=50, verbose_name='HTML Tag', choices=[(b'div', 'Division'), (b'p', 'Paragraph'), (b'h1', 'Heading 1'), (b'h2', 'Heading 2'), (b'h3', 'Heading 3'), (b'button', 'Button')])),
                ('value', models.TextField(null=True, verbose_name='Value', blank=True)),
                ('attributes', djangocms_attributes_field.fields.AttributesField(default=dict, verbose_name='Tag Attributes', blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('cms.cmsplugin',),
        ),
    ]
