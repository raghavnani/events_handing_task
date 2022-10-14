from app.models.models import Building
from app.services.abstract_service import AbstractService
from app.repo.building_repo import BuildingRepository
from app.repo.room_repo import RoomRepository


class BuildingService(AbstractService):

    def __init__(self):
        super().__init__()

    def repository(self):
        return BuildingRepository()
    
    def create_building(self, id, name, type):
        building = Building(id=id, name=name, type=type)
        return self.repository().insert(building)

    def get_all(self):
        return self.repository().find_all()

    def get_by_id(self, id):
        return self.repository().find_by_id(id)
    
    def delete_by_id(self, id):
        return self.repository().delete_by_id(id)
    
    def update_by_id(self, id, name, type):
        building = self.repository().find_by_id(id)

        if building is not None:
            building.name = name
            building.type = type
            return self.repository().update(building)
        else:
            building = Building(id=id, name=name, type=type)
            return self.repository().insert(building)

    def get_most_offices(self, type="Healthcare"):

        return self.repository().get_most_offices_with_rooms_starting_with_office(type)



