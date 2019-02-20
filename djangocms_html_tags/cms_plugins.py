from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from djangocms_html_tags.forms import HTMLTextInputForm, HTMLFormForm, HTMLTextareaForm
from djangocms_html_tags.models import HTMLTag, HTMLText
from djangocms_html_tags.utils import FormMethod


class HTMLTextBase(CMSPluginBase):
    model = HTMLText
    module = _("HTML Tags")
    render_template = 'djangocms_html_tags/html_text.html'
    fields = ('value', 'attributes')
    form = HTMLTextInputForm
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


class Heading4Plugin(HTMLTextBase):
    name = _("Heading 4")
    tag = HTMLTag.H4


class Heading5Plugin(HTMLTextBase):
    name = _("Heading 5")
    tag = HTMLTag.H5


class Heading6Plugin(HTMLTextBase):
    name = _("Heading 6")
    tag = HTMLTag.H6


class ParagraphPlugin(HTMLTextBase):
    name = _("Paragraph")
    tag = HTMLTag.P
    form = HTMLTextareaForm
    allow_children = True


class ButtonPlugin(HTMLTextBase):
    name = _("Button")
    tag = HTMLTag.BUTTON
    allow_children = True


class InputPlugin(HTMLTextBase):
    name = _("Input")
    tag = HTMLTag.INPUT
    render_template = 'djangocms_html_tags/input.html'


class FormPlugin(HTMLTextBase):
    name = _("Form")
    tag = HTMLTag.FORM
    model = HTMLText
    form = HTMLFormForm
    fields = (('method', 'action'), 'value', 'attributes')
    render_template = 'djangocms_html_tags/form.html'
    allow_children = True

    def render(self, context, instance, placeholder):
        context.update({'is_post': instance.attributes.get('method') == FormMethod.POST})
        return super(FormPlugin, self).render(context, instance, placeholder)


plugin_pool.register_plugin(Heading1Plugin)
plugin_pool.register_plugin(Heading2Plugin)
plugin_pool.register_plugin(Heading3Plugin)
plugin_pool.register_plugin(Heading4Plugin)
plugin_pool.register_plugin(Heading5Plugin)
plugin_pool.register_plugin(Heading6Plugin)
plugin_pool.register_plugin(ParagraphPlugin)
plugin_pool.register_plugin(ButtonPlugin)
plugin_pool.register_plugin(InputPlugin)
plugin_pool.register_plugin(FormPlugin)
