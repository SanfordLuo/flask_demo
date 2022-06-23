import logging
from flask import Flask
from utils import util_func, util_logger

util_logger.set_logger_config("main")
logger = logging.getLogger("main")

app = Flask(__name__)


@app.route('/sanford', methods=["GET"])
def hello_world():
    data = {'name': 'sanford'}
    logger.info('===info===')
    logger.error('===err===')

    return util_func.format_resp(data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2378, debug=True)
