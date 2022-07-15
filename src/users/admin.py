from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError

from users.models import User


class UserCreationForm(forms.ModelForm):

    password1 = forms.CharField(
        label='Password',
        widget=forms.PasswordInput
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput
    )

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

    class UserChangeForm(forms.ModelForm):

        password = ReadOnlyPasswordHashField()

        class Meta:
            model = User
            fields = (
                'email',
                'password',
                'first_name',
                'last_name',
                'is_active',
                'is_staff',
                'is_admin'
            )


class UserAdmin(BaseUserAdmin):

    list_display = ('email', 'name', 'teams')
    fieldsets = (
        (
            'Personal info',
            {'fields': ('first_name', 'last_name', 'email', 'password')}
        ),
        (
            'Permissions',
            {'fields': ('groups',)}
        ),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'first_name',
                'last_name',
                'password1',
                'password2'
            ),
        }),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

    @admin.display(empty_value='')
    def name(self, obj):
        return f'{obj.first_name.title()} '\
               f'{obj.last_name.upper()}'

    def teams(self, obj):
        return ','.join([g.name for g in obj.groups.all()]) if obj.groups.count() else ''


admin.site.register(User, UserAdmin)
# admin.site.unregister(Group)
