from django.urls import include, path

urlpatterns =[
    path('users/', include(('estate_agency.estate_agency_apps.users.urls', 'users'))),
    path('propertys/', include(('estate_agency.estate_agency_apps.property.urls', 'propertys'))),
    path('property_searches/', include(('estate_agency.estate_agency_apps.property_search.urls', 'property_searches'))),
   # path('education/', include(('education.education_apps.educa.urls', 'education'))),
]