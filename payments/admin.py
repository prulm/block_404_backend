from django.contrib import admin
from .models import *

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'building', 'collector', 'type', 'deadline', 'amount', 'isRecurring', 'recurrence_period', 'penality', 'attachment')
	list_display_links = ('id', 'building', 'name', 'collector')
	search_fields = ('building__name', 'collector__user__firstName', 'collector__user__lastName', 'name')
	list_per_page = 25
	sortable_by = 'id'

class HousePaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'amount', 'paid_by')
    list_display_links = ('id', 'house')
    search_fields = ('house__owner__firstName', 'house__owner__lastName', 'house__floorCode', 'house__description', 'house__building__name', 'amount', 'paid_by__user__firstName', 'paid_by__user__lastName')
    list_per_page = 25
    sortable_by = 'id'

class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'building', 'creator', 'name', 'description', 'commences', 'penality', 'attachment')
	list_display_links = ('id', 'building', 'name', 'creator')
	search_fields = ('building__name', 'creator__user__firstName', 'creator__user__lastName', 'name')
	list_per_page = 25
	sortable_by = 'id'

admin.site.register(Payment, PaymentAdmin)
admin.site.register(HousePayment, HousePaymentAdmin)
admin.site.register(Event, EventAdmin)