from app import db
from sqlalchemy.dialects.postgresql import UUID
from app.models.encoder import AlchemyEncoder

class Building(db.Model):
    __tablename__ = 'buildings'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String)
    type = db.Column(db.String)
    rooms = db.relationship('Room', backref='buildings', lazy=True)

class Room(db.Model):
    __tablename__ = 'rooms'
    
    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String)
    floor_number = db.Column(db.String)
    building_id = db.Column(UUID(as_uuid=True), db.ForeignKey('buildings.id'))