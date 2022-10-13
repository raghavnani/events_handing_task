
from unittest import result
from app.models.models import Building
from app.models.models import Room
from app.repo.abstract_repo import AbstractRepository
from app import db

class BuildingRepository(AbstractRepository):

    def entity(self):
        return Building

    def get_most_offices_with_rooms_starting_with_office(self, type):

        rows = db.session.query(Building.name, db.func.count(Room.id)).join(Room).filter(Building.type ==type).filter(Room.name.like("Office%")).group_by(Building.name).order_by(db.func.count(Room.id).desc()).all()
        
        result_list = []
        for row in rows:
            dict1 = {"name": row[0], "count": row[1]}
            result_list.append(dict1)

        return result_list
