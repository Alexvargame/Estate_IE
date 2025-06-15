

class PropertySearchService:

    def __init__(self, repository):
        self.repository = repository

    def create_object(self, dto):
        return self.repository.create_object(dto)

    def detail_object(self, obj):
        return self.repository.detail_object(obj)
    #
    def list_objects(self):
        return self.repository.list_objects()

    def statistic_objects(self, dto):
        return self.repository.statistic_objects(dto)

    def search_propertys(self, dto):
        return self.repository.search_propertys(dto)
    #
    # def update_object(self, dto):
    #     return self.repository.update_object(dto)
    #
    # def delete_object(self, property_id):
    #     self.repository.delete_object(property_id)