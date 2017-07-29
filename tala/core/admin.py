from django.contrib import admin

from core.models import Node


class NodeAdmin(admin.ModelAdmin):
    pass

admin.site.register(Node, NodeAdmin)
