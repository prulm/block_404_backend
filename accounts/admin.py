from django.contrib import admin
from .models import UserAccount

class UserAdmin(admin.ModelAdmin):
	list_display = ('id', 'firstName', 'lastName', 'email', 'phone', 'profilePicture', 'is_active', 'is_staff')
	list_display_links = ('id', 'firstName', 'lastName')
	search_fields = ('firstName', 'lastName', 'email', 'phone')
	list_per_page = 25
	sortable_by = 'id'

admin.site.register(UserAccount, UserAdmin)
