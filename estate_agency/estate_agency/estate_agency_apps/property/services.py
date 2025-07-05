

class PropertyService:

    def __init__(self, repository):
        self.repository = repository


    def get_main_page_indexes(self):
        return self.repository.get_main_page_indexes()

    def create_object(self, dto):
        return self.repository.create_object(dto)

    def detail_object(self, obj):
        return self.repository.detail_object(obj)

    def list_objects(self):
        return self.repository.list_objects()

    def list_objects_count_room(self, r):
        return self.repository.list_objects_count_room(r)

    def list_object_price(self, p1, p2):
        return self.repository.list_objects_price(p1, p2)

    def list_object_square(self, s1, s2):
        return self.repository.list_objects_square(s1, s2)

    def list_object_district(self, dist):
        return self.repository.list_objects_district(dist)

    def list_object_category(self, cat):
        return self.repository.list_objects_category(cat)
    def update_object(self, dto):
        return self.repository.update_object(dto)

    def delete_object(self, property_id):
        self.repository.delete_object(property_id)

    def get_fields(self):
        return self.repository.get_fields()

    def get_obj_by_id(self, obj_id):
        return self.repository.get_obj_by_id(obj_id)

class PropertyCategoryService:

    def __init__(self, repository):
        self.repository = repository
    def list_objects(self):
        return self.repository.list_objects()
    def get_object_by_transcription(self, transcription):
        return self.repository.get_object_by_transcription(transcription)

class PropertyTypeService:

    def __init__(self, repository):
        self.repository = repository
    def list_objects(self):
        return self.repository.list_objects()

    def get_object_by_transcription(self, transcription):
        return self.repository.get_object_by_transcription(transcription)
class DistrictService:

    def __init__(self, repository):
        self.repository = repository
    def list_objects(self):
        return self.repository.list_objects()
    def get_object_by_transcription(self, transcription):
        return self.repository.get_object_by_transcription(transcription)
class RepairStateService:

    def __init__(self, repository):
        self.repository = repository
    def list_objects(self):
        return self.repository.list_objects()
    def get_object_by_transcription(self, transcription):
        return self.repository.get_object_by_transcription(transcription)

class BuildingTypeService:

    def __init__(self, repository):
        self.repository = repository
    def list_objects(self):
        return self.repository.list_objects()
    def get_object_by_transcription(self, transcription):
        return self.repository.get_object_by_transcription(transcription)

class CityService:

    def __init__(self, repository):
        self.repository = repository
    # def list_objects(self):
    #     return self.repository.list_objects()
    def get_object_by_name(self, name):
        return self.repository.get_object_by_name(name)