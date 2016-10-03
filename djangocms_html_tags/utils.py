from django.utils.translation import ugettext_lazy as _


class HTMLTag(object):
    DIV = 'div'
    P = 'p'
    H1 = 'h1'
    H2 = 'h2'
    H3 = 'h3'
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
            (cls.BUTTON, _("Button")))
        return choices
