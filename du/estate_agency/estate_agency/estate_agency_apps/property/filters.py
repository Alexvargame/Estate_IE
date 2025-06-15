import django_filters


from estate_agency.estate_agency_apps.property.models import (PropertyType, PropertyCategory,
                                                            RepairState, BuildingType,
                                                            District, Property)

class PropertyFilter(django_filters.FilterSet):
    class Meta:
        model = Property
        fields = ("id", "property_type", "employee")


class PropertyTypeFilter(django_filters.FilterSet):
    class Meta:
        model = PropertyType
        fields = ("id", "name")

class PropertyCategoryFilter(django_filters.FilterSet):
    class Meta:
        model = PropertyCategory
        fields = ("id",)

class DistrictFilter(django_filters.FilterSet):
    class Meta:
        model = District
        fields = ("id", )

class BuildingTypeFilter(django_filters.FilterSet):
    class Meta:
        model = BuildingType
        fields = ("id", )

class RepairStateFilter(django_filters.FilterSet):
    class Meta:
        model = RepairState
        fields = ("id", )