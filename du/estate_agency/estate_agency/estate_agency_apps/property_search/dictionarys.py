

from estate_agency.estate_agency_apps.property_search.selectors import (property_search_list,
                                                                        property_search_get_statistic_property_type,
                                                                        property_search_get_statistic_property_category,
                                                                        property_search_get_statistic_district,
                                                                        property_search_get_statistic_repair_state,
                                                                        property_search_get_statistic_price,
                                                                        property_search_get_statistic_room_count,
                                                                        property_search_get_statistic_area,
                                                                        )


function_dict = {'property_type': property_search_get_statistic_property_type(),
                         'property_category':  property_search_get_statistic_property_category(),
                         'district': property_search_get_statistic_district(),
                         'repair_state': property_search_get_statistic_repair_state(),
                          'price': property_search_get_statistic_price(),
                           'area': property_search_get_statistic_area(),
                            'rooms_count':property_search_get_statistic_room_count(),
                            }