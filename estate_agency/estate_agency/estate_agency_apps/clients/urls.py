from django.urls import path

from .apis import (ClientRequestsListApi,
                   )

urlpatterns =[
#     path('create/', PropertySearchCreateApi.as_view(), name='property_search_create'),
#     path('<int:property_search_id>/', PropertySearchDetailApi.as_view(), name='property_searach_detail'),
      path('', ClientRequestsListApi.as_view(), name='client_requests_list'),
#     path('statistics/', PropertySearchStatisticApi.as_view(), name='property_search_statictic'),
#
]