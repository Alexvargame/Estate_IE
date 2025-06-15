from django.db import transaction

from estate_agency.estate_agency_apps.property_search.models import PropertySearchRequest

from estate_agency.estate_agency_apps.dtos.property_search.response_dto import PropertySearchDTO
from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
                                                            RepairState, BuildingType,
                                                            District, Property)
from estate_agency.estate_agency_apps.property_search.dictionarys import function_dict

from estate_agency.estate_agency_apps.property_search.selectors import search_propertys

class PropertySearchRepository:
    model = PropertySearchRequest

    @transaction.atomic
    def create_object(self, dto):

        property_search = self.model.objects.create(
            user=dto.user,
            title=dto.title,
            #property_type=PropertyType.objects.filter(id__in=list(dto.property_type)),
            #property_category=PropertyCategory.objects.filter(id__in=list(dto.property_category)),
            min_price=dto.min_price,
            max_price=dto.max_price,
            #district=District.objects.filter(id__in=list(dto.district)),
            min_total_area=dto.max_total_area,
            max_total_area=dto.max_total_area,
            min_rooms_count=dto.min_rooms_count,
            max_rooms_count=dto.max_rooms_count,
            min_total_floors=dto.min_total_floors,
            max_total_floors=dto.max_total_floors,
            #building_type=BuildingType.objects.filter(id__in=list(dto.building_type)),
            has_balcony=dto.has_balcony,
            #repair_state=RepairState.objects.filter(id__in=list(dto.repair_state)),
            min_created_at=dto.min_created_at,
            max_created_at=dto.max_created_at,
        )
        property_search.property_type.set(list(dto.property_type))
        property_search.property_category.set(list(dto.property_category))
        property_search.district.set(list(dto.district))
        property_search.building_type.set(list(dto.building_type))
        property_search.repair_state.set(list(dto.repair_state))

        return property_search

    def detail_object(self, obj):
        dto = PropertySearchDTO(
            id=obj.id,
            user=obj.user,
            title=obj.title,
            property_type=list(obj.property_type.all()),
            property_category=list(obj.property_category.all()),
            min_price=obj.min_price,
            max_price=obj.max_price,
            district=list(obj.district.all()),
            min_total_area=obj.max_total_area,
            max_total_area=obj.max_total_area,
            min_rooms_count=obj.min_rooms_count,
            max_rooms_count=obj.max_rooms_count,
            min_total_floors=obj.min_total_floors,
            max_total_floors=obj.max_total_floors,
            building_type=list(obj.building_type.all()),
            has_balcony=obj.has_balcony,
            repair_state=list(obj.repair_state.all()),
            min_created_at=obj.min_created_at,
            max_created_at=obj.max_created_at,
        )
        return dto

    def list_objects(self):
        lst_dto = []
        for obj in property_search_list(filters=None):
            tmp_dto = PropertySearchDTO(
                id=obj.id,
                user=obj.user,
                title=obj.title,
                property_type=list(obj.property_type.all()),
                property_category=list(obj.property_category.all()),
                min_price=obj.min_price,
                max_price=obj.max_price,
                district=list(obj.district.all()),
                min_total_area=obj.max_total_area,
                max_total_area=obj.max_total_area,
                min_rooms_count=obj.min_rooms_count,
                max_rooms_count=obj.max_rooms_count,
                min_total_floors=obj.min_total_floors,
                max_total_floors=obj.max_total_floors,
                building_type=list(obj.building_type.all()),
                has_balcony=obj.has_balcony,
                repair_state=list(obj.repair_state.all()),
                min_created_at=obj.min_created_at,
                max_created_at=obj.max_created_at,
            )
            lst_dto.append(tmp_dto)
        return lst_dto

    def statistic_objects(self, dto):

        statistic_dict = {}
        for k, v in dto.__dict__.items():
            if k != 'date_from' and k != 'date_to' and dto.__dict__[k]:
                statistic_dict[k] = function_dict[k]#property_search_get_statistic_property_type()
            elif k == 'date_from' or k == 'date_to':
                statistic_dict[k] = v
        return statistic_dict

    def search_propertys(self, dto):
        search_result = search_propertys(dto)
        return search_result


    # @transaction.atomic
    # def update_object(self, dto):
    #     property = self.model.objects.get(id=dto.id)
    #     for key, value in dto.__dict__.items():
    #         property.__dict__[key] = value
    #     property.save()
    #
    # @transaction.atomic
    # def delete_object(self, property_id):
    #     property = self.model.objects.get(id=property_id)
    #     property.delete()