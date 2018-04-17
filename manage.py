# coding:utf-8
import redis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


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


@app.route('/')
def index():
    redis_store.set("name", 'jason')
    return 'Jason!'


if __name__ == '__main__':
    print app.url_map
    app.run()
