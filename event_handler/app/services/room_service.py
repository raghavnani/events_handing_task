from app.models.models import Room
from app.services.abstract_service import AbstractService
from app.repo.room_repo import RoomRepository
from app.repo.building_repo import BuildingRepository


class RoomService(AbstractService):

    def __init__(self):
        super().__init__()

    def repository(self):
        return RoomRepository()
    

    def create_room(self, id, name, floor_number, building_id):

        building = BuildingRepository().find_by_id(building_id)
        room = Room(id=id, name=name, floor_number=floor_number)

        if building is not None:
            room = self.repository().insert(room)
            building.rooms.append(room)
            BuildingRepository().update(building)
            room.building_id = building.id
            return room
        else:
            return {"error": "Building not found"}
        
    def get_all(self):
        return self.repository().find_all()

    def get_by_id(self, id):
        return self.repository().find_by_id(id)

    def delete_by_id(self, id):
        return self.repository().delete_by_id(id)

    def update_by_id(self, id, name, floor_number, building_id):
        room = self.repository().find_by_id(id)

        if room is not None:
            room.name = name
            room.floor_number = floor_number
            room.building_id = building_id
            return self.repository().update(room)
        else:
            return {"error": "Room not found"}
