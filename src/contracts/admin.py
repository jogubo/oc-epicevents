from django.contrib import admin

from contracts.models import Contract


class ContractAdmin(admin.ModelAdmin):

    list_display = ('id', 'payment_due', 'client_name', 'status')

    @admin.display(empty_value='')
    def client_name(self, obj):
        return f'{obj.client.first_name.title()} '\
               f'{obj.client.last_name.upper()}'


admin.site.register(Contract, ContractAdmin)
