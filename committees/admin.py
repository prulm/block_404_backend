from django.contrib import admin
from committees.models import *

class CommitteeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'building')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'description', 'building__name')
    list_per_page = 25
    sortable_by = 'id'

class MembersAdmin(admin.ModelAdmin):
    list_display = ('id', 'resident', 'committee', 'position')
    list_display_links = ('id', 'resident')
    search_fields = ('resident__user__firstName', 'resident__user__lastName', 'committee__name', 'position')
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

class CommitteeAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee', 'file')
    list_display_links = ('id', 'committee')
    search_fields = ('committee__name', )
    list_per_page = 25
    sortable_by = 'id'

class CommitteePictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'committee', 'picture')
    list_display_links = ('id', 'committee')
    search_fields = ('committee__name', )
    list_per_page = 25
    sortable_by = 'id'

admin.site.register(Committee,  CommitteeAdmin)
admin.site.register(Member, MembersAdmin)
admin.site.register(Rule, RuleAdmin)
admin.site.register(Report, ReportAdmin)
admin.site.register(CommitteeAttachment, CommitteeAttachmentAdmin)
admin.site.register(CommitteePicture, CommitteePictureAdmin)

