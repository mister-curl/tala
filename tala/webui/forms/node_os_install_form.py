from django import forms


class NodeOsInstallForm(forms.Form):
    os = forms.CharField(max_length=100)
    username = forms.CharField(max_length=100)
