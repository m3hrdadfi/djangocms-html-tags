from cms.models import CMSPlugin, python_2_unicode_compatible
from django.db import models
from django.utils.text import Truncator
from django.utils.translation import ugettext_lazy as _, ugettext
from djangocms_attributes_field.fields import AttributesField

from djangocms_html_tags.utils import HTMLTag


@python_2_unicode_compatible
class HTMLText(CMSPlugin):
    tag = models.CharField(
        verbose_name=_("HTML Tag"), max_length=50, choices=HTMLTag.get_choices(), default=HTMLTag.DIV)
    value = models.TextField(verbose_name=_("Value"), blank=True, null=True)
    attributes = AttributesField(verbose_name=_("Tag Attributes"), blank=True)

    def __str__(self):
        return Truncator(self.value).chars(50) if self.value else ugettext("Empty")
