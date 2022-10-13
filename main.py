import logging
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from utils import util_func, util_logger
from server.router import api

util_logger.set_logger_config("proj-manage")
logger = logging.getLogger("proj-manage")

app = Flask(__name__)


def init_app():
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:jayae.22378@localhost:3306/sanford-test?charset=utf8'
    # 设置每次请求结束后会自动提交数据库的改动
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # 查询时显示原始SQL语句
    app.config['SQLALCHEMY_ECHO'] = False

    db = SQLAlchemy(app)

    app.register_blueprint(api, url_prefix="/sanford")

    return app


if __name__ == '__main__':
    app = init_app()
    app.run(host='0.0.0.0', port=2378, debug=True)
