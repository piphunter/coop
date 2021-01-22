from django.contrib import admin

from . models import *

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'member', 'mode', 'amount', 'date')
    list_display_links = ('id', 'member')
    list_filter = ('mode',)
    search_fields = ('member',)

admin.site.register(Member)
admin.site.register(Payment, PaymentAdmin)
