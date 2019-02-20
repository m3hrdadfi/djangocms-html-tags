from django import forms
from django.utils.translation import ugettext_lazy as _

from djangocms_html_tags.models import HTMLText
from djangocms_html_tags.utils import FormMethod


class HTMLTextBaseForm(forms.ModelForm):
    class Meta:
        model = HTMLText
        exclude = ("tag",)


class HTMLTextInputForm(HTMLTextBaseForm):
    def __init__(self, *args, **kwargs):
        super(HTMLTextInputForm, self).__init__(*args, **kwargs)

        self.fields["value"].widget = forms.TextInput()


class HTMLTextareaForm(HTMLTextBaseForm):
    def __init__(self, *args, **kwargs):
        super(HTMLTextareaForm, self).__init__(*args, **kwargs)

        self.fields["value"].widget = forms.Textarea({"rows": 5})


class HTMLFormForm(HTMLTextBaseForm):
    action = forms.CharField(label=_("Action"), max_length=256, required=False)
    method = forms.ChoiceField(label=_("Method"), choices=FormMethod.get_choices(), initial=FormMethod.POST)

    def __init__(self, *args, **kwargs):
        super(HTMLFormForm, self).__init__(*args, **kwargs)

        # use value as source code for for elements
        value = self.fields["value"]
        value.label = _("Source")

        # indeed, action and method are attributes. They"re manually added to create form easily.
        instance = kwargs.get("instance")
        if instance is not None:
            action = self.fields.get("action")
            action.initial = instance.attributes.pop("action", "")
            method = self.fields.get("method")
            method.initial = instance.attributes.pop("method", "")

    def clean(self):
        cleaned_data = super(HTMLFormForm, self).clean()
        cleaned_data.get("attributes").update({
            "action": cleaned_data.get("action", ""),
            "method": cleaned_data.get("method", FormMethod.POST)
        })
        return cleaned_data
