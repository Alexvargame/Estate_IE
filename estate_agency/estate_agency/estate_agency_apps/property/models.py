from django.db import models

from estate_agency.estate_agency_apps.users.models import BaseUser
class PropertyType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Тип объекта недвижимости'
        verbose_name_plural = 'Типы объектов недвижимости'

    def __str__(self):
        return self.name

class PropertyCategory(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Категория объекта недвижимости'
        verbose_name_plural = 'Категории объектов недвижимости'

    def __str__(self):
        return self.name

class City(models.Model):

    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'

    def __str__(self):
        return f'{self.name}:{self.region}'

class District(models.Model):

    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)
    description = models.TextField()

    class Meta:
        verbose_name = 'Район города'
        verbose_name_plural = 'Районы города'

    def __str__(self):
        return f'{self.name}:{self.city}'

class BuildingType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Тип материалов дома'
        verbose_name_plural = 'Типы материалов дома'

    def __str__(self):
        return self.name

class RepairState(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()

    class Meta:
        verbose_name = 'Состояние ремонта'
        verbose_name_plural = 'Состояния ремонта'

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    property_type = models.ForeignKey(PropertyType, related_name='property_types', on_delete=models.CASCADE)
    property_category = models.ForeignKey(PropertyCategory, related_name='property_categories', on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    district = models.ForeignKey(District, related_name='districts', on_delete=models.CASCADE)
    address = models.CharField(max_length=200)
    total_area = models.DecimalField(max_digits=10, decimal_places=2)
    living_area = models.DecimalField(max_digits=10, decimal_places=2)
    rooms_count = models.IntegerField()
    floor = models.IntegerField()
    total_floor = models.IntegerField()
    building_type = models.ForeignKey(BuildingType, related_name='building_types', on_delete=models.CASCADE)
    has_balcony = models.BooleanField(default=0)
    repair_state = models.ForeignKey(RepairState, related_name='repair_stetes', on_delete=models.CASCADE)
    infrastructure = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=1)
    employee = models.ForeignKey(BaseUser, related_name='employees', on_delete=models.CASCADE, default=1)


    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

    def __str__(self):
        return self.title