from django.shortcuts import render

from estate_agency.estate_agency_apps.property.services import PropertyService
from estate_agency.estate_agency_apps.property.repository import PropertyRepository

def main_page(request):
    objs = PropertyService(PropertyRepository()).get_main_page_indexes()
    print('OBJS', objs)
    return render(request, 'main_page.html', {'objs': objs})


def detail_object(request):
    return render(request, 'property/property_object_detail.html')