from dataclasses import dataclass


from estate_agency.estate_agency_apps.users.models import BaseUser
from estate_agency.estate_agency_apps.property.models import (
                                PropertyCategory, PropertyType, RepairState,
                                BuildingType, City, District,
                                )



@dataclass
class CreatePropertyDTO:
    title: str
    description: str
    property_type: PropertyType
    property_category: PropertyCategory
    price: float
    district: District
    address: str
    total_area: float
    living_area: float
    rooms_count: int
    floor: int
    total_floor: int
    building_type: BuildingType
    has_balcony: int
    repair_state: RepairState
    infrastructure: str
    is_active: int
    employee: BaseUser

