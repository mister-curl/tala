from django import forms

from core.models import VirtualMachine

from core.utils.executor import create_virtual_machine
from django.forms import Select


class VirtualMachineCreateForm(forms.ModelForm):
    class Meta:
            model = VirtualMachine
            fields = ('name', 'description', 'hostname', 'allocate_cpu', 'allocate_memory', 'allocate_disk', 'host_server', 'os', 'password')

    OS_CHOICES = (
        ('ubuntu1604_x86-64', 'Ubuntu 16.04'),
        ('ubuntu1404_x86-64', 'Ubuntu 14.04'),
    )

    os = forms.ChoiceField(widget=Select, choices=OS_CHOICES)

    def save(self, commit=True):
        # Save the provided password in hashed format
        vm = super(VirtualMachineCreateForm, self).save(commit=True)
        if commit:
            pass
        return vm
