from django import forms
from rest_api.models import SnailsActivity


class SnailActivityForm(forms.Form):
    class Meta:
        model = SnailsActivity
        fields = '__all__'
