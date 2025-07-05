from django.contrib import admin

from .models import City, District, PropertyType, PropertyCategory, RepairState, BuildingType, Property


@admin.register(PropertyType)
class PropertyTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(PropertyCategory)
class PropertyCategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'region', 'description')


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city', 'description')

@admin.register(BuildingType)
class BuildingTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')


@admin.register(RepairState)
class RepairStateAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'property_type', 'property_category',
    'district', 'address' ,'price', 'total_area', 'living_area', 'rooms_count',
    'floor', 'total_floor', 'building_type', 'repair_state', 'infrastructure',
    'created_at', 'updated_at', 'is_active' , 'employee')

