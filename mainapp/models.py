from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

db = SQLAlchemy()


def init_db(app):
    db.init_app(app)  # 初始化数据库

    Migrate(app, db)  # 创建Migrate 对象


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(10))
    phone = db.Column(db.String(20))

    __tablename__ = 'user'

    @property
    def json(self):
        return {"id": self.id,
                "name": self.name,
                "phone": self.phone}
