from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):

    list_display = ('name', 'email')

    @admin.display(empty_value='')
    def name(self, obj):
        return f'{obj.first_name.title()} '\
               f'{obj.last_name.upper()}'


admin.site.register(User)
