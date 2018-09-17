from django.core.exceptions import ValidationError
from django.forms import forms, CharField


class TodoItemForm(forms.Form):
    description = CharField(max_length=120)

    def clean(self):
        try:
            if self.cleaned_data["description"].startswith(" "):
                raise ValidationError({'name': "Input cannot start with a space"}, code='invalid')
        except KeyError:
            raise ValidationError({'name': "Description must be provided"}, code='invalid')
        return self.cleaned_data
