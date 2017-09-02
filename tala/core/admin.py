from django.contrib import admin

from core.models import Node, OS, VirtualMachine


class NodeAdmin(admin.ModelAdmin):
    pass


class OSAdmin(admin.ModelAdmin):
    pass


class VirtualMachineAdmin(admin.ModelAdmin):
    pass

admin.site.register(Node, NodeAdmin)
admin.site.register(OS, OSAdmin)
admin.site.register(VirtualMachine, VirtualMachineAdmin)
