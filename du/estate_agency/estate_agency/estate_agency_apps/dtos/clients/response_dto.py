from dataclasses import dataclass
from typing import List

from estate_agency.estate_agency_apps.users.models import BaseUser
from estate_agency.estate_agency_apps.property.models import (
                                PropertyCategory, PropertyType, District,
                                )

@dataclass
class ClientRequestsDTO:
    user: BaseUser
    property_type: List[PropertyType]
    property_category: List[PropertyCategory]
    district: List[District]
    min_created_at: str
    max_created_at: str