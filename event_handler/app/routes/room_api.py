from flask import request, Response
from flask import Blueprint
from app.services.room_service import RoomService
from app.models.encoder import AlchemyEncoder
import json



service = RoomService()
room_api = Blueprint('room_api', __name__)


@room_api.route('/api/rooms', methods=['POST'])
def create_room():

        try:
            id = request.json['room_id']
            name = request.json['name']
            floor_number = request.json['floor_number']
            building_id = request.json['building_id']
            room = service.create_room(id, name, floor_number, building_id)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

        return Response(json.dumps(room, cls=AlchemyEncoder) , status=200, content_type="application/json")


@room_api.route('/api/rooms', methods=['GET'])
def get_all():
    
        try:
            rooms = service.get_all()
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
    
        return Response(json.dumps(rooms, cls=AlchemyEncoder) , status=200, content_type="application/json")

@room_api.route('/api/rooms/<id>', methods=['GET'])
def get_by_id(id):
            try:
                room = service.get_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(room, cls=AlchemyEncoder) , status=200, content_type="application/json")

@room_api.route('/api/rooms/<id>', methods=['DELETE'])
def delete_by_id(id):
            try:
                room = service.delete_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

            return Response(json.dumps(room, cls=AlchemyEncoder) , status=200, content_type="application/json")


@room_api.route('/api/rooms/<id>', methods=['PUT'])
def update_by_id(id):
            try:
                room = service.update_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(room, cls=AlchemyEncoder) , status=200, content_type="application/json")
