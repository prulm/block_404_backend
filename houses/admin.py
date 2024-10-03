from django.contrib import admin

class HouseAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'building', 'address', 'squareFeet', 'price', 'bedrooms', 'bathrooms', 'yearBuilt', 'is_available')