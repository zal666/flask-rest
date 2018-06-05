from flask import Blueprint, Response, Flask

# 创建蓝图对象
blue = Blueprint('main', __name__)


def init_blue(app: Flask):
    app.register_blueprint(blue)


@blue.route('/')
def index():
    return Response('hi')
