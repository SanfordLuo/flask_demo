from flask import Flask
from common.utils import format_resp
from common import log_handler

logger = log_handler.Logger().logger

app = Flask(__name__)


@app.route('/sanford', methods=["GET"])
def hello_world():
    data = {'name': 'sanford'}
    logger.info('===info===')
    logger.error('===err===')

    return format_resp(data=data)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=2378, debug=True)
