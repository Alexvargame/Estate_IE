from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.mixins import LoginRequiredMixin


from estate_agency.estate_agency_apps.api.pagination import (
    LimitOffsetPagination,
    get_pagination_response,
)

from estate_agency.estate_agency_apps.property.models import Property

from estate_agency.estate_agency_apps.property.selectors import (property_get, property_type_get,
                                                                               property_category_get, district_get,
                                                                               building_type_get, repair_state_get)
from estate_agency.estate_agency_apps.users.selectors import user_get

from estate_agency.estate_agency_apps.dtos.property.response_dto import PropertyDTO

from estate_agency.estate_agency_apps.property.services import PropertyService
from estate_agency.estate_agency_apps.property.repository import PropertyRepository
from estate_agency.estate_agency_apps.dtos.property.request_dto import CreatePropertyDTO

from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
                                                            RepairState, BuildingType,
                                                            District)
from estate_agency.estate_agency_apps.users.models import BaseUser
class PropertyCreateApi(LoginRequiredMixin, LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        property_type = serializers.CharField()
        property_category = serializers.CharField()
        price = serializers.DecimalField(default=0.0, max_digits=10, decimal_places=2)
        district = serializers.CharField(allow_null=True, allow_blank=True, required=False)
        address = serializers.CharField(allow_blank=True, allow_null=True, required=False)
        total_area = serializers.DecimalField(max_digits=10, decimal_places=2)
        living_area = serializers.DecimalField(max_digits=10, decimal_places=2)
        rooms_count = serializers.IntegerField(allow_null=True, required=False)
        floor = serializers.IntegerField(allow_null=True, required=False)
        total_floor = serializers.IntegerField(allow_null=True,  required=False)
        building_type = serializers.CharField(allow_null=True,  required=False)
        has_balcony = serializers.IntegerField(allow_null=True, default=0 )
        repair_state = serializers.CharField(allow_null=True, required=False)
        infrastructure = serializers.CharField(allow_null=True, required=False)
        is_active = serializers.BooleanField(default=1)
        employee = serializers.CharField(default=1)


    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        property_type = property_type_get(serializer.validated_data['property_type'])
        serializer.validated_data['property_type'] = property_type
        property_category = property_category_get(serializer.validated_data['property_category'])
        serializer.validated_data['property_category'] = property_category
        district = district_get(serializer.validated_data['district'])
        serializer.validated_data['district'] = district
        building_type = building_type_get(serializer.validated_data['building_type'])
        serializer.validated_data['building_type'] = building_type
        repair_state = repair_state_get(serializer.validated_data['repair_state'])
        serializer.validated_data['repair_state'] = repair_state
        employee = user_get(serializer.validated_data['employee'])
        serializer.validated_data['employee'] = employee

        data = CreatePropertyDTO(
            **serializer.validated_data,
        )
        property = PropertyService(PropertyRepository()).create_object(data)
        data = PropertyDetailApi.OutputSerializer(property).data
        return Response(data)

class PropertyDetailApi(LoginRequiredMixin, LimitOffsetPagination, APIView):
    class OutputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
        title = serializers.CharField()
        description = serializers.CharField()
        property_type = serializers.CharField()
        property_category = serializers.CharField()
        price = serializers.DecimalField(max_digits=10, decimal_places=2)
        district = serializers.CharField()
        address = serializers.CharField()
        total_area = serializers.DecimalField(max_digits=10, decimal_places=2)
        living_area = serializers.DecimalField(max_digits=10, decimal_places=2)
        rooms_count = serializers.IntegerField()
        floor = serializers.IntegerField()
        total_floor = serializers.IntegerField()
        building_type = serializers.CharField()
        has_balcony = serializers.IntegerField()
        repair_state = serializers.CharField()
        infrastructure = serializers.CharField()
        is_active = serializers.BooleanField()
        employee = serializers.CharField()
        created_at = serializers.CharField()
        updated_at = serializers.CharField()
    def get(self, request, property_id):
        property = property_get(property_id)
        if property is None:
            raise Http404
        dto = PropertyService(PropertyRepository()).detail_object(property)
        data = self.OutputSerializer(dto).data
        return Response(data)


class PropertyListApi(LoginRequiredMixin, LimitOffsetPagination, APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 2

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        property_type = serializers.CharField(required=False, allow_null=True)
        employee = serializers.CharField(required=False)

    class OutputSerializer(serializers.ModelSerializer):

        class Meta:
            model = Property
            fields = ('id', 'title', 'description', 'property_type', 'property_category',
                'district', 'address' , 'total_area', 'living_area', 'rooms_count',
                'floor', 'total_floor', 'building_type', 'has_balcony', 'repair_state', 'infrastructure',
                'created_at', 'updated_at', 'is_active' , 'employee')
    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        propertys = PropertyService(PropertyRepository()).list_objects()
        #data = self.OutputSerializer(query, many=True).data
        return get_pagination_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=propertys,
            request=request,
            view=self,
        )


class PropertyUpdateApi(LoginRequiredMixin, LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        title = serializers.CharField()
        description = serializers.CharField()
        property_type = serializers.CharField()
        property_category = serializers.CharField()
        price = serializers.DecimalField(default=0.0, max_digits=10, decimal_places=2)
        district = serializers.CharField(allow_null=True, allow_blank=True, required=False)
        address = serializers.CharField(allow_blank=True, allow_null=True, required=False)
        total_area = serializers.DecimalField(max_digits=10, decimal_places=2)
        living_area = serializers.DecimalField(max_digits=10, decimal_places=2)
        rooms_count = serializers.IntegerField(allow_null=True, required=False)
        floor = serializers.IntegerField(allow_null=True, required=False)
        total_floor = serializers.IntegerField(allow_null=True, required=False)
        building_type = serializers.CharField(allow_null=True, required=False)
        has_balcony = serializers.IntegerField(allow_null=True, default=0)
        repair_state = serializers.CharField(allow_null=True, required=False)
        infrastructure = serializers.CharField(allow_null=True, required=False)
        is_active = serializers.BooleanField(default=1)
        employee = serializers.CharField(default=1)

    def post(self, request, property_id):
        property = property_get(property_id)
        merged_data = {**PropertyService(PropertyRepository()).detail_object(property).__dict__, **request.data}
        serializer = self.InputSerializer(data=merged_data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['id'] = property.id
        serializer.validated_data['created_at'] = property.created_at
        serializer.validated_data['updated_at'] = property.updated_at
        dto = PropertyDTO(
           **serializer.validated_data
        )
        PropertyService(PropertyRepository()).update_object(dto)
        property = property_get(property_id)
        data = PropertyDetailApi.OutputSerializer(property).data
        return Response(data)

class PropertyDeleteApi(LoginRequiredMixin, LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        id = serializers.IntegerField()
    class Pagination(LimitOffsetPagination):
        default_limit = 2
    class OutputSerializer(serializers.ModelSerializer):

        class Meta:
            model = Property
            fields = ('id', 'title', 'description', 'property_type', 'property_category',
                'district', 'address' , 'total_area', 'living_area', 'rooms_count',
                'floor', 'total_floor', 'building_type', 'has_balcony', 'repair_state', 'infrastructure',
                'created_at', 'updated_at', 'is_active' , 'employee')
    def post(self, request, property_id):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        PropertyService(PropertyRepository()).delete_object(serializer.validated_data['id'])
        propertys = PropertyService(PropertyRepository()).list_objects()
        # data = self.OutputSerializer(query, many=True).data
        return get_pagination_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=propertys,
            request=request,
            view=self,
        )


