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
#
# from estate_agency.estate_agency_apps.property_search.selectors import (property_search_get, )
from estate_agency.estate_agency_apps.property.selectors import (
    property_type_list, property_category_list, district_list,
)
from estate_agency.estate_agency_apps.users.selectors import user_get
#
#
# from estate_agency.estate_agency_apps.property_search.services import PropertySearchService
# from estate_agency.estate_agency_apps.property_search.repository import PropertySearchRepository
from estate_agency.estate_agency_apps.dtos.clients.response_dto import ClientRequestsDTO
# from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
#                                                             RepairState, BuildingType,
#                                                             District)
# from estate_agency.estate_agency_apps.users.models import BaseUser
#
class ClientRequestsListApi(LimitOffsetPagination, APIView):
    class InputSerializer(serializers.Serializer):
        user = serializers.CharField(default=19)
        property_type = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             property_type_list()])
        property_category = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             property_category_list()])
        district = serializers.MultipleChoiceField(choices=[(ob.id, ob.id) for ob in
                                                             district_list()])
        min_created_at = serializers.CharField(default="2015-04-15")
        max_created_at = serializers.CharField(default="2025-04-15")


    def post(self, request):
        serializer = self.InputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        print('11', serializer.validated_data)
        user = user_get(serializer.validated_data['user'])
        serializer.validated_data['user'] = user
        dto = ClientRequestsDTO(
            **serializer.validated_data,
        )
        print('CLIENT__DTO',dto)
        # property_search = PropertySearchService(PropertySearchRepository()).create_object(dto)
        # search_result = PropertySearchService(PropertySearchRepository()).search_propertys(dto)
        # data = PropertySearchDetailApi.OutputSerializer(property_search).data
        # print('property_search', search_result)
        return Response(data)
#
# class PropertySearchDetailApi(LimitOffsetPagination, APIView):
#     class OutputSerializer(serializers.Serializer):
#         user = serializers.CharField()
#         title = serializers.CharField()
#         property_type = serializers.StringRelatedField(many=True)
#         property_category = serializers.StringRelatedField(many=True)
#         min_price = serializers.DecimalField(max_digits=15, decimal_places=2)
#         max_price = serializers.DecimalField(max_digits=15, decimal_places=2)
#         district = serializers.StringRelatedField(many=True)
#         min_total_area = serializers.DecimalField(max_digits=15, decimal_places=2)
#         max_total_area = serializers.DecimalField(max_digits=15, decimal_places=2)
#         min_rooms_count = serializers.IntegerField()
#         max_rooms_count = serializers.IntegerField()
#         min_total_floors = serializers.IntegerField()
#         max_total_floors = serializers.IntegerField()
#         building_type = serializers.StringRelatedField(many=True)
#         has_balcony = serializers.BooleanField()
#         repair_state = serializers.StringRelatedField(many=True)
#         min_created_at = serializers.CharField()
#         max_created_at = serializers.CharField()
#
#     def get(self, request, property_search_id):
#         property_search = property_search_get(property_search_id)
#         if property_search is None:
#             raise Http404
#         dto = PropertySearchService(PropertySearchRepository()).detail_object(property_search)
#         data = self.OutputSerializer(dto).data
#         return Response(data)
#
#
# class PropertySearchListApi(LimitOffsetPagination, APIView):
#
#     class Pagination(LimitOffsetPagination):
#         default_limit = 2
#
#     class FilterSerializer(serializers.Serializer):
#         id = serializers.IntegerField(required=False)
#         property_type = serializers.CharField(required=False, allow_null=True)
#
#
#     class OutputSerializer(serializers.ModelSerializer):
#
#         class Meta:
#             model = PropertySearchRequest
#             fields = ('id', 'user_id', 'get_property_types', 'get_property_categories', 'min_price','max_price', 'get_districts', 'min_total_area',
#                     'max_total_area', 'min_rooms_count', 'max_rooms_count', 'min_total_floors',
#                     'max_total_floors', 'get_building_types', 'has_balcony','get_repair_states', 'additional_requirements',
#                     'min_created_at', 'max_created_at')
#     def get(self, request):
#         filters_serializer = self.FilterSerializer(data=request.query_params)
#         filters_serializer.is_valid(raise_exception=True)
#         property_searches = PropertySearchService(PropertySearchRepository()).list_objects()
#         #data = self.OutputSerializer(query, many=True).data
#         return get_pagination_response(
#             pagination_class=self.Pagination,
#             serializer_class=self.OutputSerializer,
#             queryset=property_searches,
#             request=request,
#             view=self,
#         )
#

# class PropertySearchStatisticApi(LoginRequiredMixin, LimitOffsetPagination, APIView):
#
#     class Paginaiton(LimitOffsetPagination):
#         default_limit = 2
#
#     class InputSerializer(serializers.Serializer):
#         date_from = serializers.CharField()
#         date_to = serializers.CharField()
#         property_type = serializers.BooleanField(default=False)
#         property_category = serializers.BooleanField(default=False)
#         district = serializers.BooleanField(default=False)
#         repair_state = serializers.BooleanField(default=False)
#         area = serializers.BooleanField(default=False)
#         rooms_count = serializers.BooleanField(default=False)
#         price = serializers.BooleanField(default=False)
#
#     class FilterSerializer(serializers.Serializer):
#         id = serializers.IntegerField(required=False)
#         property_type = serializers.CharField(required=False, allow_null=True)
#
#     class OutputSerializer(serializers.Serializer):
#         date_from = serializers.CharField()
#         date_to = serializers.CharField()
#         property_type = serializers.CharField()
#         property_category = serializers.CharField()
#         district = serializers.CharField()
#         repair_state = serializers.CharField()
#         price = serializers.CharField()
#         area = serializers.CharField()
#         rooms_count = serializers.CharField()
#
#     def post(self, request):
#
#         serializer = self.InputSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         dto = PropertySearchStatisticDTO(
#             **serializer.validated_data
#         )
#         statistic = PropertySearchService(PropertySearchRepository()).statistic_objects(dto)
#         print('STAT', statistic)
#         data = self.OutputSerializer(statistic).data
#         print(dto)
#         print(data)
#         print(serializer.validated_data)
#
#         return Response(data)
