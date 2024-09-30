from django.contrib import admin
from .models import *

class BuildingAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'description', 'housesPerFloor', 'floors', 'address')
	list_display_links = ('id', 'name')
	search_fields = ('name', 'address')
	list_per_page = 25
	sortable_by = 'id'

admin.site.register(Building, BuildingAdmin)