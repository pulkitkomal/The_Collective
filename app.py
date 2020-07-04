from flask import Flask
from services.user_services import user_ser
from services.collective_services import collection
from flask_cors import CORS

tcr = Flask(__name__)
CORS(tcr)
tcr.register_blueprint(user_ser)
tcr.register_blueprint(collection)


@tcr.route('/')
def test():
    return "I'm back bitches"


if __name__ == '__main__':
    tcr.run(host='0.0.0.0', port=5000)