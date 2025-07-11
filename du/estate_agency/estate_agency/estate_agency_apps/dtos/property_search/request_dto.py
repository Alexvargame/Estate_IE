from dataclasses import dataclass
from typing import List

from estate_agency.estate_agency_apps.users.models import BaseUser
from estate_agency.estate_agency_apps.property.models import (
                                PropertyCategory, PropertyType, RepairState,
                                BuildingType, City, District,
                                )

@dataclass
class CreatePropertySearchDTO:
    user: BaseUser
    title: str
    property_type: List[PropertyType]
    property_category: List[PropertyCategory]
    min_price: float
    max_price: float
    district: List[District]
    min_total_area: float
    max_total_area: float
    min_rooms_count: int
    max_rooms_count: int
    min_total_floors: int
    max_total_floors: int
    building_type: List[BuildingType]
    has_balcony: int
    repair_state: List[RepairState]
    min_created_at: str
    max_created_at: str