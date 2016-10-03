from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from djangocms_html_tags.models import HTMLTag, HTMLText
from django.utils.translation import ugettext_lazy as _


class HTMLTextBase(CMSPluginBase):
    model = HTMLText
    module = _("HTML Tags")
    render_template = 'djangocms_html_tags/html_text.html'
    fields = ('value', 'attributes')
    tag = None

    def save_model(self, request, obj, form, change):
        obj.tag = self.tag
        return super(HTMLTextBase, self).save_model(request, obj, form, change)


class Heading1Plugin(HTMLTextBase):
    name = _("Heading 1")
    tag = HTMLTag.H1


class Heading2Plugin(HTMLTextBase):
    name = _("Heading 2")
    tag = HTMLTag.H2


class Heading3Plugin(HTMLTextBase):
    name = _("Heading 3")
    tag = HTMLTag.H3


class ParagraphPlugin(HTMLTextBase):
    name = _("Paragraph")
    tag = HTMLTag.P
    allow_children = True


class ButtonPlugin(HTMLTextBase):
    name = _("Button")
    tag = HTMLTag.BUTTON
    allow_children = True


plugin_pool.register_plugin(Heading1Plugin)
plugin_pool.register_plugin(Heading2Plugin)
plugin_pool.register_plugin(Heading3Plugin)
plugin_pool.register_plugin(ParagraphPlugin)
plugin_pool.register_plugin(ButtonPlugin)
