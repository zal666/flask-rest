from flask_script import Manager
from flask_migrate import MigrateCommand
from mainapp import create_app

app = create_app()
manage = Manager(app)  # 创建manage管理器

# 向manager 添加db的命令

manage.add_command('db', MigrateCommand)

# 命令行

# Python manage.py db -?
# python manage.py db init  初始化数据库环境
# python manage.py db migrate  生成表的迁移计划
# python manage.py db upgrade 执行新的迁移计划
# python manage.py db downgrade 执行之前的迁移计划

if __name__ == '__main__':
    manage.run()
