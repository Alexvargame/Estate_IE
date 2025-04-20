from typing import Optional

from django.db.models.query import QuerySet

from estate_agency.estate_agency_apps.common.utils import get_object
from estate_agency.estate_agency_apps.property_search.models import PropertySearchRequest
from estate_agency.estate_agency_apps.property_search.filters import PropertySearchFilter
from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
                                                            RepairState, BuildingType,
                                                            District, Property)

# def user_get_login_data(*, user):
#     return {
#         'id': user.id,
#         'email': user.email,
#         'is_active': user.is_active,
#         "is_admin": user.is_admin,
#         "is_superuser": user.is_superuser,
# #     }
def property_search_list(*, filters=None):
    filters = filters or {}
    qs = PropertySearchRequest.objects.all()
    return PropertySearchFilter(filters, qs).qs

def property_search_get(property_search_id):
    property_search = get_object(PropertySearchRequest, id=property_search_id)
    return property_search

# def property_type_get(property_type_id):
#     property_type = get_object(PropertyType, id=property_type_id)
#     return property_type
#
# def property_category_get(property_category_id):
#     property_category = get_object(PropertyCategory, id=property_category_id)
#     return property_category
#
# def district_get(district_id):
#     district = get_object(District, id=district_id)
#     return district
#
# def building_type_get(building_type_id):
#     building_type = get_object(BuildingType, id=building_type_id)
#     return building_type
#
# def repair_state_get(repair_state_id):
#     repair_state = get_object(RepairState, id=repair_state_id)
#     return repair_state












