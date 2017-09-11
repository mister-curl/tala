from django import forms
from django.contrib import admin

from core.models import Node, OS, VirtualMachine

from core.models import User
from django.contrib.auth.admin import UserAdmin


class NodeAdmin(admin.ModelAdmin):
    pass


class OSAdmin(admin.ModelAdmin):
    pass


class VirtualMachineAdmin(admin.ModelAdmin):
    pass


class UserCreateForm(forms.ModelForm):
    """ユーザ追加のためのフォーム。パスワードがハッシュで保存されないため追加しました。"""

    class Meta:
            model = User
            fields = ('username', 'first_name', 'last_name', 'email', 'password', 'ssh_public_key')

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(UserCreateForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user


class CustomUserAdmin(UserAdmin):
    add_form = UserCreateForm

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'ssh_public_key')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password', 'first_name', 'last_name', 'ssh_public_key', 'is_superuser', 'is_staff', 'is_active')}
         ),
    )

    filter_horizontal = ()


admin.site.register(Node, NodeAdmin)
admin.site.register(OS, OSAdmin)
admin.site.register(VirtualMachine, VirtualMachineAdmin)
admin.site.register(User, CustomUserAdmin)
