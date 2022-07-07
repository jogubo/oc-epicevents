from django.contrib import admin

from events.models import Event


class EventAdmin(admin.ModelAdmin):

    list_display = ('event_date', 'client_name')

    @admin.display(empty_value='')
    def client_name(self, obj):
        return f'{obj.client.first_name.title()} '\
               f'{obj.client.last_name.upper()}'


admin.site.register(Event, EventAdmin)
