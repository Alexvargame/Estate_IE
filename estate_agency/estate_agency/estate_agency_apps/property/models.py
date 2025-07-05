from django.db import models

from estate_agency.estate_agency_apps.users.models import BaseUser
class PropertyType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    transcription = models.CharField(max_length=100, default='')
    #description = models.CharField(max_length=100, default='')


    class Meta:
        verbose_name = 'Тип объекта недвижимости'
        verbose_name_plural = 'Типы объектов недвижимости'

    def __str__(self):
        return self.name

class PropertyCategory(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    transcription = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Категория объекта недвижимости'
        verbose_name_plural = 'Категории объектов недвижимости'

    def __str__(self):
        return self.name

class City(models.Model):

    name = models.CharField(max_length=100)
    region = models.CharField(max_length=100)
    description = models.TextField()
    transcription = models.CharField(max_length=100, default='')

    class Meta:
        verbose_name = 'Населенный пункт'
        verbose_name_plural = 'Населенные пункты'


    def __str__(self):
        return f'{self.name}:{self.region}'

class District(models.Model):

    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, related_name='districts', on_delete=models.CASCADE)
    description = models.TextField()
    transcription = models.CharField(max_length=100, default='')


    class Meta:
        verbose_name = 'Район города'
        verbose_name_plural = 'Районы города'

    def __str__(self):
        #return f'{self.name}:{self.city}'
        return f"{self.name}"

class BuildingType(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    transcription = models.CharField(max_length=100, default='')


    class Meta:
        verbose_name = 'Тип материалов дома'
        verbose_name_plural = 'Типы материалов дома'

    def __str__(self):
        return self.name

class RepairState(models.Model):

    name = models.CharField(max_length=100)
    description = models.TextField()
    transcription = models.CharField(max_length=100, default='')


    class Meta:
        verbose_name = 'Состояние ремонта'
        verbose_name_plural = 'Состояния ремонта'

    def __str__(self):
        return self.name

class Property(models.Model):
    title = models.CharField(max_length=100, verbose_name="Название объявления", )
    description = models.TextField(blank=True, null=True, verbose_name="Описание",)
    property_type = models.ForeignKey(PropertyType, verbose_name="Тип объекта", related_name='property_types',
                                      on_delete=models.CASCADE, default=1)
    property_category = models.ForeignKey(PropertyCategory, verbose_name="Категория объекта", related_name='property_categories',
                                          on_delete=models.CASCADE)
    price = models.DecimalField(decimal_places=2, max_digits=10, verbose_name="Цена",)
    district = models.ForeignKey(District, related_name='districts', on_delete=models.CASCADE, verbose_name="Район города")
    address = models.CharField(max_length=200, blank=True, null=True, verbose_name="Адрес",)
    total_area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Общая площадь",)
    living_area = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Жилая площадь",)
    rooms_count = models.IntegerField(verbose_name="Кол-во комнат")
    floor = models.IntegerField(verbose_name="Этаж")
    total_floor = models.IntegerField(verbose_name="Этажность")
    building_type = models.ForeignKey(BuildingType, verbose_name="Материал стен", related_name='building_types',
                                      on_delete=models.CASCADE)
    repair_state = models.ForeignKey(RepairState, verbose_name="Ремонт", related_name='repair_stetes',
                                     on_delete=models.CASCADE)
    infrastructure = models.TextField(blank=True, null=True, verbose_name="Инфраструктура",)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Создан",)
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Исправлен",)
    is_active = models.BooleanField(default=1, verbose_name="Активность",)
    employee = models.ForeignKey(BaseUser, verbose_name="Автор", related_name='employees',
                                 on_delete=models.CASCADE, default=1)


    class Meta:
        verbose_name = 'Объект недвижимости'
        verbose_name_plural = 'Объекты недвижимости'

    def __str__(self):
        return self.title