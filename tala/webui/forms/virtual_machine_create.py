from django import forms

from core.models import VirtualMachine

from core.utils.executor import create_virtual_machine


class VirtualMachineCreateForm(forms.ModelForm):
    class Meta:
            model = VirtualMachine
            fields = ('name', 'host_server', )

    def save(self, commit=True):
        # Save the provided password in hashed format
        vm = super(VirtualMachineCreateForm, self).save(commit=False)
        create_virtual_machine.delay(1, "test")
        if commit:
            vm.save()
        return vm
