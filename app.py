from flask import Flask

tcr = Flask(__name__)

@tcr.route('/')
def test():
    return "I'm back bitches"


if __name__ == '__main__':
    tcr.run()
    