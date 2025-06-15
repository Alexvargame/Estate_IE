# from typing import Optional
#
# from django.db.models.query import QuerySet
#
# from estate_agency.estate_agency_apps.common.utils import get_object
# from estate_agency.estate_agency_apps.property_search.models import PropertySearchRequest
# from estate_agency.estate_agency_apps.property_search.filters import PropertySearchFilter
# from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
#                                                             RepairState, BuildingType,
#                                                             District, Property)
#
# # def user_get_login_data(*, user):
# #     return {
# #         'id': user.id,
# #         'email': user.email,
# #         'is_active': user.is_active,
# #         "is_admin": user.is_admin,
# #         "is_superuser": user.is_superuser,
# # #     }
# def property_search_list(*, filters=None):
#     filters = filters or {}
#     qs = PropertySearchRequest.objects.all()
#     return PropertySearchFilter(filters, qs).qs
#
# def property_search_get(property_search_id):
#     property_search = get_object(PropertySearchRequest, id=property_search_id)
#     return property_search
#
# def property_search_get_statistic_property_type():
#     type_dict = dict.fromkeys([obj.name for obj in PropertyType.objects.all()], 0)
#     for srq in PropertySearchRequest.objects.all():
#         for type in srq.get_property_types():
#             type_dict[type.name] += 1
#     return type_dict
#
# def property_search_get_statistic_property_category():
#     category_dict = dict.fromkeys([obj.name for obj in PropertyCategory.objects.all()], 0)
#     for srq in PropertySearchRequest.objects.all():
#         for cat in srq.get_property_categories():
#             category_dict[cat.name] += 1
#     return category_dict
#
#
# def property_search_get_statistic_district():
#     district_dict = dict.fromkeys([obj.name for obj in District.objects.all()], 0)
#     for srq in PropertySearchRequest.objects.all():
#         for dist in srq.get_districts():
#             district_dict[dist.name] += 1
#     return district_dict
#
# def property_search_get_statistic_repair_state():
#     repair_dict = dict.fromkeys([obj.name for obj in RepairState.objects.all()], 0)
#     for srq in PropertySearchRequest.objects.all():
#         for dist in srq.get_repair_states():
#             repair_dict[dist.name] += 1
#     return repair_dict
#
# def property_search_get_statistic_price():
#     price_dict = {}
#     for srq in PropertySearchRequest.objects.all():
#         for pr in range(int(srq.min_price), int(srq.max_price)+500, 500):
#
#             if price_dict.get(pr):
#                 price_dict[pr] += 1
#             else:
#                 price_dict[pr] = 1
#     return price_dict
#
# def property_search_get_statistic_area():
#     area_dict = {}
#     for srq in PropertySearchRequest.objects.all():
#         for ar in range(int(srq.min_total_area), int(srq.max_total_area)+5, 5):
#
#             if area_dict.get(ar):
#                 area_dict[ar] += 1
#             else:
#                 area_dict[ar] = 1
#     return area_dict
#
# def property_search_get_statistic_room_count():
#     rooms_dict = {}
#     for srq in PropertySearchRequest.objects.all():
#         for r in range(srq.min_rooms_count, srq.max_rooms_count+1, 1):
#
#             if rooms_dict.get(r):
#                 rooms_dict[r] += 1
#             else:
#                 rooms_dict[r] = 1
#     return rooms_dict
#
# def search_propertys(dto):
#     search_result = Property.objects.filter(property_category__in=list(dto.property_category),
#                                                          property_type__in=list(dto.property_type),
#                                                          repair_state__in=list(dto.repair_state),
#                                                          building_type__in=list(dto.building_type),
#                                                          district__in=list(dto.district),
#                                                          price__range=[dto.min_price, dto.max_price],
#                                                          total_area__range=[dto.min_total_area, dto.max_total_area],
#                                                          rooms_count__range=[dto.min_rooms_count, dto.max_rooms_count],
#                                                          total_floor__range=[dto.min_total_floors, dto.max_total_floors],
#                                                          created_at__range=[dto.min_created_at, dto.max_created_at],
#                                                          )
#     return search_result
#
#
#
#
#
#
#


