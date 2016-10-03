from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_html_tags.models import HTMLTag
from django.utils.translations import ugettext_lazy as _


class HTMLTagBase(CMSPluginBase):
    model = HTMLTag
    render_template = 'djangocms_html_tags/default/html_tag.html'
    fields = ('value', 'attributes')
    tag = None

    def save_model(self, request, obj, form, change):
        obj.tag = self.tag
        return super(HTMLElementPluginBase, self).save_model(request, obj, form, change)


class Heading1Plugin(HTMLElementPluginBase):
    name = _("Heading 1")
    tag = HTMLTag.H1


class Heading2Plugin(HTMLElementPluginBase):
    name = _("Heading 2")
    tag = HTMLTag.H2


class Heading3Plugin(HTMLElementPluginBase):
    name = _("Heading 3")
    tag = HTMLTag.H3


class ParagraphPlugin(HTMLElementPluginBase):
    name = _("Paragraph")
    tag = HTMLTag.P
    allow_children = True


class ButtonPlugin(HTMLElementPluginBase):
    name = _("Button")
    tag = HTMLTag.BUTTON
    allow_children = True


plugin_pool.register_plugin(Heading1Plugin)
plugin_pool.register_plugin(Heading2Plugin)
plugin_pool.register_plugin(Heading3Plugin)
plugin_pool.register_plugin(ParagraphPlugin)
plugin_pool.register_plugin(ButtonPlugin)
