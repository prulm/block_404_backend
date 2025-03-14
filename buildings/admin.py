from django.contrib import admin
from .models import *

class BuildingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'housesPerFloor', 'floors', 'location')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'location')
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


class PenalityAdmin(admin.ModelAdmin):
	list_display = ('id', 'reason', 'amount')
	list_display_links = ('id', )
	search_fields = ('reason', )
	list_per_page = 25
	sortable_by = 'id'

admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingAttachment, BuildingAttachmentAdmin)
admin.site.register(BuildingPicture, BuildingPictureAdmin)
admin.site.register(Penality, PenalityAdmin)