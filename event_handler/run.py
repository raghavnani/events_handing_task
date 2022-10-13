from app import app
from app.routes.building_api import building_api
from app.routes.room_api import room_api
from flask_socketio import SocketIO
from app.services.building_service import BuildingService
from app.services.room_service import RoomService


socketio = SocketIO(app, cors_allowed_origins='*')



building_service = BuildingService()
room_service = RoomService()

@socketio.on('room')
def room_message(data):

    print('received json: ', data['response'])

    room = data['response']["payload"]

    if data['response']['action'] == 'created':
        room_service.create_room(room['room_id'], room['name'], room['floor_number'], room['building_id'])
    elif data['response']['action'] == 'deleted':
        pass
        #room_service.delete_by_id(room['room_id'])
    elif data['response']['action'] == 'updated':
        room_service.update_by_id(room['room_id'], room['name'], room['floor_number'], room['building_id'])

# @socketio.on('building')
# def building_message(data):

#     building = data['response']["payload"]

#     if data['response']['action'] == 'created':
#         resp = building_service.create_building(building['building_id'], building['name'], building['type'])
#     elif data['response']['action'] == 'deleted':
#         pass
#         #resp =building_service.delete_by_id(building['building_id'])
#     elif data['response']['action'] == 'updated':
#         resp = building_service.update_by_id(building['building_id'], building['name'], building['type'])

if __name__ == '__main__':


    app.register_blueprint(building_api)
    app.register_blueprint(room_api)
    
    # Run the application
    app.run(host="0.0.0.0", debug=True, port=4000)

