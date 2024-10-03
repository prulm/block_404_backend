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
    list_per_page = 25
    sortable_by = 'id'

class RuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee', 'rule', 'order', 'picture')
    list_display_links = ('id', 'committee')
    search_fields = ('committee__name', 'rule')
    list_per_page = 25
    sortable_by = 'id'

class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee', 'title', 'description', 'file')
    list_display_links = ('id', 'committee', 'title')
    search_fields = ('committee__name', 'title', 'description')
    list_per_page = 25
    sortable_by = 'id'

class CommitteeAttachmentModel(admin.ModelAdmin):
    list_display = ('id', 'committee', 'attachment')
    list_display_links = ('id', 'committee')
    search_fields = ('committee__name', )
    list_per_page = 25
    sortable_by = 'id'

class CommitteePictureModel(admin.ModelAdmin):
    list_display = ('id', 'committee', 'picture')
    list_display_links = ('id', 'committee')
    search_fields = ('committee__name', )
    list_per_page = 25
    sortable_by = 'id'

