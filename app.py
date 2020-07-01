from flask import Flask
from services.user_services import user_ser

tcr = Flask(__name__)
tcr.register_blueprint(user_ser)


@tcr.route('/')
def test():
    return "I'm back bitches"


if __name__ == '__main__':
    tcr.run(host='0.0.0.0', port=5000)