from flask import Flask

from mainapp import views, models, settings

from flask_session import Session

from flask_debugtoolbar import DebugToolbarExtension


def create_app():
    app = Flask(__name__)

    app.env = 'development'

    dt = DebugToolbarExtension()
    dt.init_app(app)

    # 从类中获取config配置的属性
    app.config.from_object(settings.Config)

    #  相关的初始化
    models.init_db(app)
    views.init_blue(app)

    Session(app)  # 初始化session

    return app
