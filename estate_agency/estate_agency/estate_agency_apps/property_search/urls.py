from django.urls import path

from .apis import (PropertySearchDetailApi, PropertySearchCreateApi,
                    PropertySearchListApi, PropertySearchStatisticApi

                   )

urlpatterns =[
    path('create/', PropertySearchCreateApi.as_view(), name='property_search_create'),
    path('<int:property_search_id>/', PropertySearchDetailApi.as_view(), name='property_searach_detail'),
    path('', PropertySearchListApi.as_view(), name='property_searches_list'),
    path('statistics/', PropertySearchStatisticApi.as_view(), name='property_search_statictic'),
    # path('<int:property_id>/update/', PropertyUpdateApi.as_view(), name='property_update'),
    # path('<int:property_id>/delete/', PropertyDeleteApi.as_view(), name='property_delete'),
]