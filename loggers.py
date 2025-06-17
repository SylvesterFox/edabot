import json
import logging
import logging.config

from settings import config

bot = logging.getLogger('bot')

def setup():
    dict_config = json.load(open(config.LOGGING_CONF_FILE, 'r'))
    logging.config.dictConfig(
        config=dict_config
    )