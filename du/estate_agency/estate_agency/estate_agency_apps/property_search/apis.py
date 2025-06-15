from django.http import Http404
from rest_framework import serializers
from rest_framework.response import Response
from rest_framework.views import APIView

from django.contrib.auth.mixins import LoginRequiredMixin

from estate_agency.estate_agency_apps.api.pagination import (
    LimitOffsetPagination,
    get_pagination_response,
)

from estate_agency.estate_agency_apps.property_search.models import PropertySearchRequest

from estate_agency.estate_agency_apps.property_search.selectors import (property_search_get, )
from estate_agency.estate_agency_apps.property.selectors import (
    property_type_list, property_category_list, district_list,
    building_type_list, property_list, repair_state_list,
)
from estate_agency.estate_agency_apps.users.selectors import user_get


from estate_agency.estate_agency_apps.property_search.services import PropertySearchService
from estate_agency.estate_agency_apps.property_search.repository import PropertySearchRepository
from estate_agency.estate_agency_apps.dtos.property_search.request_dto import CreatePropertySearchDTO
from estate_agency.estate_agency_apps.dtos.property_search.response_dto import PropertySearchStatisticDTO

from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
                                                            RepairState, BuildingType,
                                                            District)
from estate_agency.estate_agency_apps.users.models import BaseUser

class PropertySearchCreateApi(LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        user = serializers.CharField(default=19)
        title = serializers.CharField()
        property_type = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             property_type_list()])
        property_category = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             property_category_list()])
        min_price = serializers.DecimalField(max_digits=15, decimal_places=2, default=1)
        max_price = serializers.DecimalField(max_digits=15, decimal_places=2, default=1000000)
        district = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             district_list()])
        min_total_area = serializers.DecimalField(max_digits=15, decimal_places=2, default=1)
        max_total_area = serializers.DecimalField(max_digits=15, decimal_places=2, default=1000)
        min_rooms_count = serializers.IntegerField(default=1)
        max_rooms_count = serializers.IntegerField(default=10)
        min_total_floors = serializers.IntegerField(default=1)
        max_total_floors = serializers.IntegerField(default=50)
        building_type = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in building_type_list()])
        has_balcony = serializers.BooleanField(default=False)
        repair_state = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             repair_state_list()])
        min_created_at = serializers.CharField(default="2015-04-15")
        max_created_at = serializers.CharField(default="2025-04-15")


    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('11', serializer.validated_data)
        user = user_get(serializer.validated_data['user'])
        serializer.validated_data['user'] = user
        dto = CreatePropertySearchDTO(
            **serializer.validated_data,
        )
        property_search = PropertySearchService(PropertySearchRepository()).create_object(dto)
        search_result = PropertySearchService(PropertySearchRepository()).search_propertys(dto)
        data = PropertySearchDetailApi.OutputSerializer(property_search).data
        print('property_search', search_result)
        return Response(data)

class PropertySearchDetailApi(LimitOffsetPagination, APIView):
    class OutputSerializer(serializers.Serializer):
        user = serializers.CharField()
        title = serializers.CharField()
        property_type = serializers.StringRelatedField(many=True)
        property_category = serializers.StringRelatedField(many=True)
        min_price = serializers.DecimalField(max_digits=15, decimal_places=2)
        max_price = serializers.DecimalField(max_digits=15, decimal_places=2)
        district = serializers.StringRelatedField(many=True)
        min_total_area = serializers.DecimalField(max_digits=15, decimal_places=2)
        max_total_area = serializers.DecimalField(max_digits=15, decimal_places=2)
        min_rooms_count = serializers.IntegerField()
        max_rooms_count = serializers.IntegerField()
        min_total_floors = serializers.IntegerField()
        max_total_floors = serializers.IntegerField()
        building_type = serializers.StringRelatedField(many=True)
        has_balcony = serializers.BooleanField()
        repair_state = serializers.StringRelatedField(many=True)
        min_created_at = serializers.CharField()
        max_created_at = serializers.CharField()

    def get(self, request, property_search_id):
        property_search = property_search_get(property_search_id)
        if property_search is None:
            raise Http404
        dto = PropertySearchService(PropertySearchRepository()).detail_object(property_search)
        data = self.OutputSerializer(dto).data
        return Response(data)


class PropertySearchListApi(LimitOffsetPagination, APIView):

    class Pagination(LimitOffsetPagination):
        default_limit = 2

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        property_type = serializers.CharField(required=False, allow_null=True)


    class OutputSerializer(serializers.ModelSerializer):

        class Meta:
            model = PropertySearchRequest
            fields = ('id', 'user_id', 'get_property_types', 'get_property_categories', 'min_price','max_price', 'get_districts', 'min_total_area',
                    'max_total_area', 'min_rooms_count', 'max_rooms_count', 'min_total_floors',
                    'max_total_floors', 'get_building_types', 'has_balcony','get_repair_states', 'additional_requirements',
                    'min_created_at', 'max_created_at')
    def get(self, request):
        filters_serializer = self.FilterSerializer(data=request.query_params)
        filters_serializer.is_valid(raise_exception=True)
        property_searches = PropertySearchService(PropertySearchRepository()).list_objects()
        #data = self.OutputSerializer(query, many=True).data
        return get_pagination_response(
            pagination_class=self.Pagination,
            serializer_class=self.OutputSerializer,
            queryset=property_searches,
            request=request,
            view=self,
        )

# class PropertySearchSeasrchApi(LimitOffsetPagination, APIView):
#
#     class InputSerializer(serializers.Serializer):
#
#
# class PropertyUpdateApi(LimitOffsetPagination, APIView):
#     class InputSerializer(serializers.Serializer):
#         title = serializers.CharField()
#         description = serializers.CharField()
#         property_type = serializers.CharField()
#         property_category = serializers.CharField()
#         price = serializers.DecimalField(default=0.0, max_digits=10, decimal_places=2)
#         district = serializers.CharField(allow_null=True, allow_blank=True, required=False)
#         address = serializers.CharField(allow_blank=True, allow_null=True, required=False)
#         total_area = serializers.DecimalField(max_digits=10, decimal_places=2)
#         living_area = serializers.DecimalField(max_digits=10, decimal_places=2)
#         rooms_count = serializers.IntegerField(allow_null=True, required=False)
#         floor = serializers.IntegerField(allow_null=True, required=False)
#         total_floor = serializers.IntegerField(allow_null=True, required=False)
#         building_type = serializers.CharField(allow_null=True, required=False)
#         has_balcony = serializers.IntegerField(allow_null=True, default=0)
#         repair_state = serializers.CharField(allow_null=True, required=False)
#         infrastructure = serializers.CharField(allow_null=True, required=False)
#         is_active = serializers.BooleanField(default=1)
#         employee = serializers.CharField(default=1)
#
#     def post(self, request, property_id):
#         property = property_get(property_id)
#         merged_data = {**PropertyService(PropertyRepository()).detail_object(property).__dict__, **request.data}
#         serializer = self.InputSerializer(data=merged_data)
#         serializer.is_valid(raise_exception=True)
#         serializer.validated_data['id'] = property.id
#         serializer.validated_data['created_at'] = property.created_at
#         serializer.validated_data['updated_at'] = property.updated_at
#         dto = PropertyDTO(
#            **serializer.validated_data
#         )
#         PropertyService(PropertyRepository()).update_object(dto)
#         property = property_get(property_id)
#         data = PropertyDetailApi.OutputSerializer(property).data
#         return Response(data)
#
# class PropertyDeleteApi(LimitOffsetPagination, APIView):
#     class InputSerializer(serializers.Serializer):
#         id = serializers.IntegerField()
#     class Pagination(LimitOffsetPagination):
#         default_limit = 2
#     class OutputSerializer(serializers.ModelSerializer):
#
#         class Meta:
#             model = Property
#             fields = ('id', 'title', 'description', 'property_type', 'property_category',
#                 'district', 'address' , 'total_area', 'living_area', 'rooms_count',
#                 'floor', 'total_floor', 'building_type', 'has_balcony', 'repair_state', 'infrastructure',
#                 'created_at', 'updated_at', 'is_active' , 'employee')
#     def post(self, request, property_id):
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         PropertyService(PropertyRepository()).delete_object(serializer.validated_data['id'])
#         propertys = PropertyService(PropertyRepository()).list_objects()
#         # data = self.OutputSerializer(query, many=True).data
#         return get_pagination_response(
#             pagination_class=self.Pagination,
#             serializer_class=self.OutputSerializer,
#             queryset=propertys,
#             request=request,
#             view=self,
#         )
#
#
class PropertySearchStatisticApi(LoginRequiredMixin, LimitOffsetPagination, APIView):

    class Paginaiton(LimitOffsetPagination):
        default_limit = 2

    class InputSerializer(serializers.Serializer):
        date_from = serializers.CharField()
        date_to = serializers.CharField()
        property_type = serializers.BooleanField(default=False)
        property_category = serializers.BooleanField(default=False)
        district = serializers.BooleanField(default=False)
        repair_state = serializers.BooleanField(default=False)
        area = serializers.BooleanField(default=False)
        rooms_count = serializers.BooleanField(default=False)
        price = serializers.BooleanField(default=False)

    class FilterSerializer(serializers.Serializer):
        id = serializers.IntegerField(required=False)
        property_type = serializers.CharField(required=False, allow_null=True)

    class OutputSerializer(serializers.Serializer):
        date_from = serializers.CharField()
        date_to = serializers.CharField()
        property_type = serializers.CharField()
        property_category = serializers.CharField()
        district = serializers.CharField()
        repair_state = serializers.CharField()
        price = serializers.CharField()
        area = serializers.CharField()
        rooms_count = serializers.CharField()

    def post(self, request):

        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        dto = PropertySearchStatisticDTO(
            **serializer.validated_data
        )
        statistic = PropertySearchService(PropertySearchRepository()).statistic_objects(dto)
        print('STAT', statistic)
        data = self.OutputSerializer(statistic).data
        print(dto)
        print(data)
        print(serializer.validated_data)

        return Response(data)
