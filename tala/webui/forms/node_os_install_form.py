from django import forms
from django.forms import Select


class NodeOsInstallForm(forms.Form):
    OS_CHOICES = (
        ('ubuntu1604_x86-64', 'Ubuntu 16.04'),
        ('ubuntu1404_x86-64', 'Ubuntu 14.04'),
    )

    os = forms.ChoiceField(widget=Select, choices=OS_CHOICES)
    username = forms.CharField(max_length=100)
