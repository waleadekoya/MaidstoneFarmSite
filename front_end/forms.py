from django import forms
from django.forms import widgets, DateTimeInput

from rest_api.models import SnailsActivity


class SnailActivityForm(forms.ModelForm):
    class Meta:
        model = SnailsActivity
        fields = '__all__'
        widgets = {
            "dateTimeRecorded": DateTimeInput(attrs={'type': 'datetime-local'})
        }

    def __init__(self, *args, **kwargs):
        super(SnailActivityForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            if field == "dateTimeRecorded":
                # https://stackoverflow.com/a/18680374
                self.fields[field].widget = DateTimeInput(attrs={'type': 'datetime-local'})
            if field == "comments":
                self.fields[field].required = False
            self.fields[field].widget.attrs.update({'class': 'form-control'})
