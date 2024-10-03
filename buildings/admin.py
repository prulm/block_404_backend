from django.contrib import admin
from .models import *

class BuildingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'housesPerFloor', 'floors', 'address')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'address')
	list_per_page = 25
	sortable_by = 'id'

class BuildingAttachmentAdmin(admin.ModelAdmin):
	list_display = ('id', 'building', 'file')	
	list_display_links = ('id', 'building')
	search_fields = ('building__name', 'file')
	list_per_page = 25
	sortable_by = 'id'

class BuildingPictureAdmin(admin.ModelAdmin):
	list_display = ('id', 'building', 'picture')
	list_display_links = ('id', 'building')
	search_fields = ('building__name', 'picture')
	list_per_page = 25
	sortable_by = 'id'

class EventAdmin(admin.ModelAdmin):
	list_display = ('id', 'building', 'creator', 'name', 'description', 'commences', 'penality', 'attachment')
	list_display_links = ('id', 'building', 'name', 'creator')
	search_fields = ('building__name', 'creator__firstName', 'name')
	list_per_page = 25
	sortable_by = 'id'

class PaymentAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'building', 'collector', 'type', 'deadline', 'amount', 'isRecurring', 'recurrence_period', 'penality', 'attachment')
	list_display_links = ('id', 'building', 'name', 'collector')
	search_fields = ('building__name', 'collector__firstName', 'name')
	list_per_page = 25
	sortable_by = 'id'

class PenalityAdmin(admin.ModelAdmin):
	list_display = ('id', 'building', 'reason', 'amount')
	list_display_links = ('id', 'building')
	search_fields = ('building__name','reason')
	list_per_page = 25
	sortable_by = 'id'

admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingAttachment, BuildingAttachmentAdmin)
admin.site.register(BuildingPicture, BuildingPictureAdmin)
admin.site.register(Event, EventAdmin)
admin.site.register(Payment, PaymentAdmin)
admin.site.register(Penality, PenalityAdmin)