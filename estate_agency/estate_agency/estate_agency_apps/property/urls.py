from django.urls import path

from .apis import (PropertyCreateApi, PropertyDetailApi,
                   PropertyListApi, PropertyUpdateApi,
                   PropertyDeleteApi)

urlpatterns =[
    path('create/', PropertyCreateApi.as_view(), name='property_create'),
    path('<int:property_id>/', PropertyDetailApi.as_view(), name='property_detail'),
    path('', PropertyListApi.as_view(), name='propertys_list'),
    path('<int:property_id>/update/', PropertyUpdateApi.as_view(), name='property_update'),
    path('<int:property_id>/delete/', PropertyDeleteApi.as_view(), name='property_delete'),
]