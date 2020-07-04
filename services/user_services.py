from flask import Blueprint, request, Response
from mongo_services import users
import json
user_ser = Blueprint('users', __name__)


@user_ser.route('/create_user', methods=['POST'])
def create_new_user():
    data = request.get_json()
    # username = data['username']
    # password = data['password']
    # email = data['email']
    username = request.form['username']
    password = request.form['password']
    email = request.form['email']
    temp_var = users.User().create_user(username, email, password)
    if temp_var[0]:
        res = json.dumps(temp_var[1])
        return Response(response=res, mimetype='application/json', status=200)
        # return res
    else:
        res = json.dumps(temp_var[1])
        return Response(response=res, mimetype='application/json')
        # return res


@user_ser.route('/login', methods=['POST'])
def create_session():
    # data = request.get_json()
    # username = data['username']
    # password = data['password']
    username = request.form['username']
    password = request.form['password']
    temp_var = users.User().login(username, password)
    if temp_var[0]:
        res = json.dumps(temp_var[1])
        return Response(response=res, mimetype='application/json', status=200)
    else:
        res = json.dumps(temp_var[1])
        return Response(response=res, mimetype='application/json')
