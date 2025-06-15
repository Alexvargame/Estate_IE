from django.db import transaction

import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate_agency.config.django.base')
django.setup()

from estate_agency.estate_agency_apps.property.models import (Property, PropertyType,
                                                            PropertyCategory,
                                                              )

from estate_agency.estate_agency_apps.dtos.property.response_dto import PropertyDTO
from estate_agency.estate_agency_apps.dtos.property_types.response_dto import PropertyTypesDTO
from estate_agency.estate_agency_apps.dtos.property_category.response_dto import PropertyCategoryDTO
from estate_agency.estate_agency_apps.property.selectors import (property_list, property_type_list,
                                                                property_category_list,
                                                                 )

class PropertyRepository:
    model = Property

    @transaction.atomic
    def create_object(self, dto):

        property = self.model.objects.create(
            title=dto.title,
            description = dto.description,
            property_type = dto.property_type,
            property_category = dto.property_category,
            price = dto.price,
            district = dto.district,
            address = dto.address,
            total_area = dto.total_area,
            living_area = dto.living_area,
            rooms_count = dto.rooms_count,
            floor = dto.floor,
            total_floor = dto.total_floor,
            building_type = dto.building_type,
            has_balcony = dto.has_balcony,
            repair_state = dto.repair_state,
            infrastructure = dto.infrastructure,
            is_active = dto.is_active,
            employee = dto.employee
        )

        return property

    def detail_object(self, obj):
        dto = PropertyDTO(
            id=obj.id,
            title=obj.title,
            description=obj.description,
            property_type=obj.property_type,
            property_category=obj.property_category,
            price=obj.price,
            district=obj.district,
            address=obj.address,
            total_area=obj.total_area,
            living_area=obj.living_area,
            rooms_count=obj.rooms_count,
            floor=obj.floor,
            total_floor=obj.total_floor,
            building_type=obj.building_type,
            has_balcony=obj.has_balcony,
            repair_state=obj.repair_state,
            infrastructure=obj.infrastructure,
            is_active=obj.is_active,
            employee=obj.employee,
            created_at=obj.created_at,
            updated_at=obj.updated_at,
        )
        return dto

    def list_objects(self):
        lst_dto = []
        for obj in property_list(filters=None):
            tmp_dto = PropertyDTO(
                id=obj.id,
                title=obj.title,
                description=obj.description,
                property_type=obj.property_type,
                property_category=obj.property_category,
                price=obj.price,
                district=obj.district,
                address=obj.address,
                total_area=obj.total_area,
                living_area=obj.living_area,
                rooms_count=obj.rooms_count,
                floor=obj.floor,
                total_floor=obj.total_floor,
                building_type=obj.building_type,
                has_balcony=obj.has_balcony,
                repair_state=obj.repair_state,
                infrastructure=obj.infrastructure,
                is_active=obj.is_active,
                employee=obj.employee,
                created_at=obj.created_at,
                updated_at=obj.updated_at,
            )
            lst_dto.append(tmp_dto)
        return lst_dto

    @transaction.atomic
    def update_object(self, dto):
        property = self.model.objects.get(id=dto.id)
        for key, value in dto.__dict__.items():
            property.__dict__[key] = value
        property.save()

    @transaction.atomic
    def delete_object(self, property_id):
        property = self.model.objects.get(id=property_id)
        property.delete()

class PropertyTypeRepository:
    model = PropertyType

    def list_objects(self):
        dto_list = []
        for obj in property_type_list(filters=None):
            tmp_dto = PropertyTypesDTO(
                id=obj.id,
                name=obj.name,
                description=obj.description,
                transcription=obj.transcription
            )
            dto_list.append(tmp_dto)
        return dto_list

class PropertyCategoryRepository:
    model = PropertyCategory

    def list_objects(self):
        dto_list = []
        for obj in property_category_list(filters=None):
            print([p.transcription for p in property_category_list()])
            tmp_dto = PropertyCategoryDTO(
                id=obj.id,
                name=obj.name,
                description=obj.description,
                transcription=obj.transcription
            )
            dto_list.append(tmp_dto)
        return dto_list