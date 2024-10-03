from django.contrib import admin

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'building')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'building__name')
    list_per_page = 25
    sortable_by = 'id'

class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'committee', 'position')
    list_display_links = ('id', 'user')
    search_fields = ('user__firstName', 'user__lastName', 'committee__name', 'position')