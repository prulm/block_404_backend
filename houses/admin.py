from django.contrib import admin
from houses.models import *

class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'floor', 'floorCode', 'description', 'building', 'squareMeter', 'bedrooms', 'status')
    list_display_links = ('id', 'owner', 'floor', 'floorCode')
    search_fields = ('owner__firstName', 'owner__lastName', 'floorCode', 'description', 'building__name')
    list_per_page = 25
    sortable_by = 'id'

class HouseAttachmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'file')
    list_display_links = ('id', 'house')
    search_fields = ('house__owner__firstName', 'house__owner__lastName', 'house__floorCode', 'house__description', 'house__building__name')
    list_per_page = 25
    sortable_by = 'id'

class HousePictureAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'picture')
    list_display_links = ('id', 'house')
    search_fields = ('house__owner__firstName', 'house__owner__lastName', 'house__floorCode', 'house__description', 'house__building__name')
    list_per_page = 25
    sortable_by = 'id'

class ResidentAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'user', 'isOwner', 'isHead', 'isActive')
    list_display_links = ('id', 'house', 'user')
    search_fields = ('house__owner__firstName', 'house__owner__lastName', 'house__floorCode', 'house__description', 'house__building__name', 'user__firstName', 'user__lastName')
    list_per_page = 25
    sortable_by = 'id'

class HousePenalityAdmin(admin.ModelAdmin):
    list_display = ('id', 'house', 'penality', 'is_paid')
    list_display_links = ('id', 'house')
    search_fields = ('house__owner__firstName', 'house__owner__lastName', 'house__floorCode', 'house__description', 'house__building__name', 'penality__reason', 'is_paid')
    list_per_page = 25
    sortable_by = 'id'

admin.site.register(House, HouseAdmin)
admin.site.register(HouseAttachment, HouseAttachmentAdmin)
admin.site.register(HousePicture, HousePictureAdmin)
admin.site.register(Resident, ResidentAdmin)
admin.site.register(HousePenality, HousePenalityAdmin)