from django.urls import path

from .apis import (PropertyCreateApi, PropertyDetailApi,
                   PropertyListApi, PropertyUpdateApi,
                   PropertyDeleteApi)

from .apis_frontend import PropertyDetailApiFrontEnd
#from estate_agency.estate_agency_apps.api.views import main_page, detail_object
app_name = 'propertys'

urlpatterns =[
    #path('', main_page, name='main_page'),
    path('create/', PropertyCreateApi.as_view(), name='property_create'),
    path('<int:property_id>/', PropertyDetailApi.as_view(), name='property_detail'),
    path('', PropertyListApi.as_view(), name='propertys_list'),
    path('<int:property_id>/update/', PropertyUpdateApi.as_view(), name='property_update'),
    path('<int:property_id>/delete/', PropertyDeleteApi.as_view(), name='property_delete'),


    path('fr/<int:property_id>/', PropertyDetailApiFrontEnd.as_view(), name='property_detail_frontend'),

]