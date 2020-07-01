from pymongo import MongoClient
from config import monogoDB, db, user, password_key, session_key
import re
from cryptography.fernet import Fernet
import jwt
import datetime
f = Fernet(password_key)


def verify_password(password):
    if len(password) < 8:
        return False
    else:
        return True


def check_email(email):
    if re.findall('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email):
        return True
    else:
        return False


def create_session(username):
    exp = datetime.datetime.utcnow() + datetime.timedelta(days=3)
    payload = {'username': username, 'exp': exp}
    token = jwt.encode(payload, session_key, algorithm='HS256')
    return token


def verify_session(token):
    try:
        jwt.decode(token, session_key, algorithms='HS256')
        return True
    except:
        return False

class User:
    def __init__(self):
        client = MongoClient(monogoDB)
        tcr = client[db]
        self.user = tcr[user]

    def check_username(self, username):
        query = {'username': username}
        for username_obj in self.user.find(query):
            if username_obj['username'] == username:
                return False
            else:
                return True
        return True

    def verify_email(self, email):
        query = {'email': email}
        for email_obj in self.user.find(query):
            if email_obj['email'] == email:
                return False
            else:
                return True
        return True

    def check_password(self, username, password):
        query = {'username': username}
        for obj in self.user.find(query):
            pass_enc = obj['password']
            password_dec = f.decrypt(pass_enc)
            if password_dec == bytes(password, 'utf-8'):
                return True
            else:
                return False

    def create_user(self, username, email, password):
        if self.check_username(username):
            if check_email(email):
                if self.verify_email(email):
                    if verify_password(password):
                        password_enc = f.encrypt(bytes(password, 'utf-8'))
                        query = {'username': username.strip(), 'email': email, 'password': password_enc}
                        self.user.insert_one(query)
                        return True, 'user created successfully'
                    else:
                        return False, 'Try another password'
                else:
                    return False, 'Email already used'
            else:
                return False, 'Email not valid'
        else:
            return False, 'Try another username'

    def login(self, username, password):
        if not self.check_username(username):
            if self.check_password(username, password):
                session = create_session(username)
                return True, {'username': username, 'session_token': session}
            else:
                return False, 'Password incorrect'
        else:
            return False, 'Username incorrect'




# print(User().create_user('test2', 'test@testp.com', '12345678'))
# print(User().check_username('test'))
# print(User().login('test2', '12345678'))
# a = create_session('pulkit')
