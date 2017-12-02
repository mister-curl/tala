from django import forms

from core.models import VirtualMachine

from core.utils.executor import create_virtual_machine
from django.forms import Select

from core.models import Container


class ContainerCreateForm(forms.ModelForm):
    class Meta:
            model = Container
            fields = ('name', 'description', 'hostname', 'docker_host', 'os', 'password')

    OS_CHOICES = (
        ('ubuntu1604_x86-64', 'Ubuntu 16.04'),
    )

    os = forms.ChoiceField(widget=Select, choices=OS_CHOICES)

    def save(self, commit=True):
        container = super(ContainerCreateForm, self).save(commit=True)
        #create_virtual_machine.delay(1, "test")
        if commit:
            pass
        return container
