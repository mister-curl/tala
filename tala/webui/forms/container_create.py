from core.models import Container
from core.utils.executor import create_container
from django import forms
from django.forms import Select


class ContainerCreateForm(forms.ModelForm):
    class Meta:
            model = Container
            fields = ('name', 'description', 'hostname', 'docker_host', 'os', 'password')

    OS_CHOICES = (
        ('ubuntu1604_x86-64', 'Ubuntu 16.04'),
        ('ubuntu1404_x86-64', 'Ubuntu 14.04'),
    )

    os = forms.ChoiceField(widget=Select, choices=OS_CHOICES)

    def save(self, commit=True):
        container = super(ContainerCreateForm, self).save(commit=True)
        create_container.delay(container.id)
        if commit:
            pass
        return container
