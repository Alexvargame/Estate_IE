from typing import Optional

from django.db.models.query import QuerySet

from estate_agency.estate_agency_apps.common.utils import get_object
from estate_agency.estate_agency_apps.property.filters import (PropertyFilter, PropertyTypeFilter,
                                                                             PropertyCategoryFilter, DistrictFilter,
                                                                             RepairStateFilter, BuildingTypeFilter)
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
def property_list(*, filters=None):
    filters = filters or {}
    qs = Property.objects.all()
    return PropertyFilter(filters, qs).qs

def property_type_list(*, filters=None):
    filters = filters or {}
    qs = PropertyType.objects.all()
    return PropertyTypeFilter(filters, qs).qs

def property_category_list(*, filters=None):
    filters = filters or {}
    qs = PropertyCategory.objects.all()
    return PropertyCategoryFilter(filters, qs).qs

def district_list(*, filters=None):
    filters = filters or {}
    qs = District.objects.all()
    return DistrictFilter(filters, qs).qs

def building_type_list(*, filters=None):
    filters = filters or {}
    qs = BuildingType.objects.all()
    return BuildingTypeFilter(filters, qs).qs

def repair_state_list(*, filters=None):
    filters = filters or {}
    qs = RepairState.objects.all()
    return RepairStateFilter(filters, qs).qs

def property_get(property_id):
    property = get_object(Property, id=property_id)
    return property

def property_type_get(property_type_id):
    property_type = get_object(PropertyType, id=property_type_id)
    return property_type

def property_category_get(property_category_id):
    property_category = get_object(PropertyCategory, id=property_category_id)
    return property_category

def district_get(district_id):
    district = get_object(District, id=district_id)
    return district

def building_type_get(building_type_id):
    building_type = get_object(BuildingType, id=building_type_id)
    return building_type

def repair_state_get(repair_state_id):
    repair_state = get_object(RepairState, id=repair_state_id)
    return repair_state












