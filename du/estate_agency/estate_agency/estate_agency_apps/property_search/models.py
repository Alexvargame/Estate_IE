from django.db import models

from estate_agency.estate_agency_apps.users.models import BaseUser
from estate_agency.estate_agency_apps.property.models import (Property, PropertyType,
                                                                            PropertyCategory, District,
                                                                            RepairState, BuildingType)

class PropertySearchRequest(models.Model):

    user = models.ForeignKey(BaseUser, related_name='user_requests', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    property_type = models.ManyToManyField(PropertyType, related_name='search_property_type')
    property_category = models.ManyToManyField(PropertyCategory, related_name='search_property_category')
    min_price = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    max_price = models.DecimalField(max_digits=15, decimal_places=2, default=100000000.00)
    district = models.ManyToManyField(District, related_name='search_district')
    min_total_area = models.DecimalField(max_digits=15, decimal_places=2, default=0.00)
    max_total_area = models.DecimalField(max_digits=15, decimal_places=2, default=10000.00)
    min_rooms_count = models.IntegerField(default=0)
    max_rooms_count = models.IntegerField(default=10)
    #floor =
    min_total_floors = models.IntegerField(default=0)
    max_total_floors = models.IntegerField(default=0)
    building_type = models.ManyToManyField(BuildingType, related_name='search_building_type')
    has_balcony = models.BooleanField(default=False)
    repair_state = models.ManyToManyField(RepairState, related_name='search_repair_state')
    additional_requirements = models.TextField(blank=True, null=True)
    #status = models.
    min_created_at = models.DateField()
    max_created_at = models.DateField()

    class Meta:
        verbose_name = 'Поисковый запрос'
        verbose_name_plural = 'Поисковые запросы'

    def __str__(self):
        return self.title

    def get_property_types(self):
        return [pr_t for pr_t in self.property_type.all()]

    def get_property_categories(self):
        return [pr_c for pr_c in self.property_category.all()]


    def get_districts(self):
        return [d for d in self.district.all()]

    def get_building_types(self):
        return [b_t for b_t in self.building_type.all()]

    def get_repair_states(self):
        return [r_s for r_s in self.repair_state.all()]