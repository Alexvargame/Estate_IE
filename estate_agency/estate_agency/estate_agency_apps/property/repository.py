from django.db import transaction

import random
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'estate_agency.config.django.base')
django.setup()

from estate_agency.estate_agency_apps.property.models import (Property, PropertyType,
                                                            PropertyCategory, District,
                                                            BuildingType, RepairState,
                                                            City
                                                              )

from estate_agency.estate_agency_apps.dtos.property.response_dto import PropertyDTO
from estate_agency.estate_agency_apps.dtos.property_types.response_dto import PropertyTypesDTO
from estate_agency.estate_agency_apps.dtos.property_category.response_dto import PropertyCategoryDTO
from estate_agency.estate_agency_apps.dtos.repair_state.response_dto import RepairStateDTO
from estate_agency.estate_agency_apps.dtos.building_type.response_dto import BuildingTypeDTO
from estate_agency.estate_agency_apps.dtos.district.response_dto import DistrictDTO

from estate_agency.estate_agency_apps.property.selectors import (property_list, property_type_list,
                                                                property_category_list, district_list,
                                                                building_type_list, repair_state_list,
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
                repair_state=obj.repair_state,
                infrastructure=obj.infrastructure,
                is_active=obj.is_active,
                employee=obj.employee,
                created_at=obj.created_at,
                updated_at=obj.updated_at,
            )
            lst_dto.append(tmp_dto)
        return lst_dto

    def list_objects_count_room(self, r):
        lst_dto = []
        for obj in property_list(filters=None):
            if r > 3:
                if obj.rooms_count >= r:
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
                        repair_state=obj.repair_state,
                        infrastructure=obj.infrastructure,
                        is_active=obj.is_active,
                        employee=obj.employee,
                        created_at=obj.created_at,
                        updated_at=obj.updated_at,
                    )
                    lst_dto.append(tmp_dto)
            else:
                if obj.rooms_count == r:
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
                        repair_state=obj.repair_state,
                        infrastructure=obj.infrastructure,
                        is_active=obj.is_active,
                        employee=obj.employee,
                        created_at=obj.created_at,
                        updated_at=obj.updated_at,
                    )
                    lst_dto.append(tmp_dto)

        return lst_dto
    def get_obj_by_id(self, obj_id):
        obj = self.model.objects.get(id=obj_id)
        return obj

    def list_objects_price(self, p1, p2):
        lst_dto = []
        for obj in property_list(filters=None):
            if obj.price >= p1 and obj.price <= p2:
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
                    repair_state=obj.repair_state,
                    infrastructure=obj.infrastructure,
                    is_active=obj.is_active,
                    employee=obj.employee,
                    created_at=obj.created_at,
                    updated_at=obj.updated_at,
                )
                lst_dto.append(tmp_dto)

        return lst_dto

    def list_objects_square(self, s1, s2):
        lst_dto = []
        for obj in property_list(filters=None):
            if obj.total_area >= s1 and obj.total_area <= s2:
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
                    repair_state=obj.repair_state,
                    infrastructure=obj.infrastructure,
                    is_active=obj.is_active,
                    employee=obj.employee,
                    created_at=obj.created_at,
                    updated_at=obj.updated_at,
                )
                lst_dto.append(tmp_dto)

        return lst_dto

    def list_objects_district(self, dist):
        lst_dto = []

        for obj in property_list(filters=None):
            if obj.district.name == dist:
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
                    repair_state=obj.repair_state,
                    infrastructure=obj.infrastructure,
                    is_active=obj.is_active,
                    employee=obj.employee,
                    created_at=obj.created_at,
                    updated_at=obj.updated_at,
                )
                lst_dto.append(tmp_dto)
        return lst_dto

    def list_objects_category(self, cat):
        lst_dto = []
        for obj in property_list(filters=None):
            if obj.property_category.name == cat:
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

    def get_fields(self):
        return self.model._meta.fields

    def get_main_page_indexes(self):
        property_ids = [obj.id for obj in self.list_objects()]
        random.shuffle(property_ids)
        random_ids = property_ids[:3]
        randon_obj = [self.get_obj_by_id(idx) for idx in random_ids]
        return randon_obj


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
    def get_object_by_transcription(self, transcription):
        obj = self.model.objects.get(transcription=transcription)
        return obj

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
    def get_object_by_transcription(self, transcription):
        obj = self.model.objects.get(transcription=transcription)
        return obj
class DistrictRepository:
    model = District

    def list_objects(self):
        dto_list = []
        for obj in district_list(filters=None):
            print([p.transcription for p in district_list()])
            tmp_dto = DistrictDTO(
                id=obj.id,
                name=obj.name,
                city=obj.city,
                description=obj.description,
                transcription=obj.transcription
            )
            dto_list.append(tmp_dto)
        return dto_list
    def get_object_by_transcription(self, transcription):
        obj = self.model.objects.get(transcription=transcription)
        return obj
class RepairStateRepository:
    model = RepairState

    def list_objects(self):
        dto_list = []
        for obj in repair_state_list(filters=None):
            print([p.transcription for p in repair_state_list()])
            tmp_dto = RepairStateDTO(
                id=obj.id,
                name=obj.name,
                description=obj.description,
                transcription=obj.transcription
            )
            dto_list.append(tmp_dto)
        return dto_list
    def get_object_by_transcription(self, transcription):
        obj = self.model.objects.get(transcription=transcription)
        return obj
class BuildingTypeRepository:
    model = BuildingType
    def list_objects(self):
        dto_list = []
        for obj in building_type_list(filters=None):
            print([p.transcription for p in building_type_list()])
            tmp_dto = BuildingTypeDTO(
                id=obj.id,
                name=obj.name,
                description=obj.description,
                transcription=obj.transcription
            )
            dto_list.append(tmp_dto)
        return dto_list

    def get_object_by_transcription(self, transcription):
        obj = self.model.objects.get(transcription=transcription)
        return obj

class CityRepository:
    model = City
    # def list_objects(self):
    #     dto_list = []
    #     for obj in building_type_list(filters=None):
    #         print([p.transcription for p in building_type_list()])
    #         tmp_dto = BuildingTypeDTO(
    #             id=obj.id,
    #             name=obj.name,
    #             description=obj.description,
    #             transcription=obj.transcription
    #         )
    #         dto_list.append(tmp_dto)
    #     return dto_list

    def get_object_by_name(self, name):
        obj = self.model.objects.get(name=name)
        return obj