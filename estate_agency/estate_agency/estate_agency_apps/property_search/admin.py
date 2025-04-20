from django.contrib import admin

from estate_agency.estate_agency_apps.property_search.models import PropertySearchRequest


@admin.register(PropertySearchRequest)
class PropertySearchRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_id', 'get_property_types', 'get_property_categories', 'min_price','max_price', 'get_districts', 'min_total_area',
                    'max_total_area', 'min_rooms_count', 'max_rooms_count', 'min_total_floors',
                    'max_total_floors', 'get_building_types', 'has_balcony','get_repair_states', 'additional_requirements',
                    'min_created_at', 'max_created_at')
