
from app.models.models import Room
from app.repo.abstract_repo import AbstractRepository

class RoomRepository(AbstractRepository):

    def entity(self):
        return Room




