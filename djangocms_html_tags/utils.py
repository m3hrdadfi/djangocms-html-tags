from django.utils.translation import ugettext_lazy as _


class HTMLTag(object):
    DIV = 'div'
    P = 'p'
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
    H4 = 'h4'
    H5 = 'h5'
    H6 = 'h6'
    FORM = 'form'
    BUTTON = 'button'
    INPUT = 'input'

    @classmethod
    def get_choices(cls):
        choices = (
            (cls.DIV, _("Division")),
            (cls.P, _("Paragraph")),
            (cls.H1, _("Heading 1")),
            (cls.H2, _("Heading 2")),
            (cls.H3, _("Heading 3")),
            (cls.H4, _("Heading 4")),
            (cls.H5, _("Heading 5")),
            (cls.H6, _("Heading 6")),
            (cls.FORM, _("Form")),
            (cls.BUTTON, _("Button")),
            (cls.INPUT, _("Input")))
        return choices


class FormMethod(object):
    GET = 'get'
    POST = 'post'

    @classmethod
    def get_choices(cls):
        choices = (
            (cls.GET, _("GET")),
            (cls.POST, _("POST")))
        return choices
