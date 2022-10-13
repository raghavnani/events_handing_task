from app.services.building_service import BuildingService
from flask import request, Response, jsonify
# from app.models.alchemy_encoder import AlchemyEncoder, DecimalEncoder
from flask import Blueprint
from app.services.building_service import BuildingService
# from app.services.event_service import EventService
from app.models.encoder import AlchemyEncoder
import json



service = BuildingService()
building_api = Blueprint('building_api', __name__)


@building_api.route('/api/buildings', methods=['POST'])
def create_building():

        try:

            print(request.json)

            id = request.json['building_id']
            name = request.json['name']
            type = request.json['type']
            building = service.create_building(id, name, type)
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

        return Response(json.dumps(building, cls=AlchemyEncoder) , status=200, content_type="application/json")


@building_api.route('/api/buildings', methods=['GET'])
def get_all():
    
        try:
            buildings = service.get_all()
        except Exception as e:
            return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
    
        return Response(json.dumps(buildings, cls=AlchemyEncoder) , status=200, content_type="application/json")

@building_api.route('/api/buildings/<id>', methods=['GET'])
def get_by_id(id):
            try:
                building = service.get_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(building, cls=AlchemyEncoder) , status=200, content_type="application/json")

@building_api.route('/api/buildings/<id>', methods=['DELETE'])
def delete_by_id(id):
            try:
                building = service.delete_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")

            return Response(json.dumps(building, cls=AlchemyEncoder) , status=200, content_type="application/json")


@building_api.route('/api/buildings/<id>', methods=['PUT'])
def update_by_id(id):
            try:
                building = service.update_by_id(id)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(building, cls=AlchemyEncoder) , status=200, content_type="application/json")


@building_api.route('/api/buildings/street', methods=['GET'])
def get_street_with_most_offices():
            try:
                building = service.get_most_offices()

                print(building)
            except Exception as e:
                return Response(response=json.dumps({'message': 'Error', 'error': str(e)}), status=500, content_type="application/json")
        
            return Response(json.dumps(building) , status=200, content_type="application/json")

