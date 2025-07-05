from django.urls import include, path

from .views import main_page, detail_object
urlpatterns =[

    path('', main_page, name='main_page'),
    path('detail/', detail_object, name='detail_object'),
    path('users/', include(('estate_agency.estate_agency_apps.users.urls', 'users'), namespace='users')),
    #path('propertys/', include(('estate_agency.estate_agency_apps.property.urls','propertys'), namespace='propertys')),
    #path('propertys/', include('estate_agency.estate_agency_apps.property.urls')),
    path('propertys/', include(('estate_agency.estate_agency_apps.property.urls', 'propertys'), namespace='propertys')),
    path('property_searches/', include('estate_agency.estate_agency_apps.property_search.urls', 'property_searches')),
    path('clients/', include('estate_agency.estate_agency_apps.clients.urls', 'clients')),
]