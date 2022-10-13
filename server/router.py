import logging
from flask import Blueprint
from utils import util_func

logger = logging.getLogger("server")

api = Blueprint("api", __name__)


@api.route('/test', methods=["GET"])
def hello_world():
    data = {'name': 'sanford'}
    logger.info('===info===')
    logger.error('===err===')

    return util_func.format_resp(data=data)
