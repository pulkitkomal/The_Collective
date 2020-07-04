from flask import Blueprint, request, Response
from mongo_services import users
from mongo_services import collective
import json
from bson import json_util
collection = Blueprint('collection', __name__)


@collection.route('/add_message', methods=['POST'])
def create_message():
    data = request.get_json()
    username = data['username']
    session = data['session_token']
    message = data['message']
    group_name = data['group']
    if users.verify_session(session):
        message_response = collective.Collectives(group_name).add_message(username, message)
        if message_response[0]:
            res = json.dumps(message_response[1])
            return Response(response=res, mimetype='application', status=201)
        else:
            res = json.dumps('Message not added')
            return Response(response=res, mimetype='application/json', status=400)
    else:
        res = json.dumps('Session not valid')
        return Response(response=res, mimetype='application/json', status=401)


@collection.route('/show_message', methods=['POST'])
def show_all():
    data = request.get_json()
    username = data['username']
    group = data['group']
    session = data['session_token']
    if users.verify_session(session):
        res = json.dumps([collective.Collectives(group).show_messages()[1], username], default=json_util.default)
        return Response(response=res, mimetype='application/json', status=200)
    else:
        res = json.dumps('No messages')
        return Response(response=res, mimetype='application/json', status=404)