from django.contrib import admin

from clients.models import Client


class ClientAdmin(admin.ModelAdmin):

    list_display = ('name', 'compagny_name', 'email')
    list_filter = ('last_name', 'compagny_name')

    @admin.display(empty_value='')
    def name(self, obj):
        return f'{obj.first_name.title()} {obj.last_name.upper()}'


admin.site.register(Client, ClientAdmin)
