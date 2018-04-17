# coding:utf-8
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand


class Config(object):
    """配置配置参数"""
    DEGUG = True
    # 2.1.配置mysql数据库

    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'mysql://127.0.0.1:3306/iHome_gz01'
    # 3.1配置redis数据库
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379


app = Flask(__name__, )

# 1.加载配置仓库
app.config.from_object(Config)
# 2.创建连接到mysql的数据库对象
db = SQLAlchemy(app)
# 3.创建连接到redis的数据库对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 4.创建一个脚本管理器
manage = Manager(app)
# 5.让迁移时,app和db建立关系[app在前面]
Migrate(app, db)
# 6.将数据库迁移命令脚本，命令添加到脚本管理器
manage.add_command(db, MigrateCommand)


@app.route('/')
def index():
    redis_store.set("name", 'jason')
    return 'Jason!'


if __name__ == '__main__':
    print app.url_map
    # 记得edit_configration中加载script_params 配置runserver
    manage.run()
