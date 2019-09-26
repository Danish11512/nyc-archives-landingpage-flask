import os
from flask import Flask

app = Flask(__name__)

if os.getenv('LANDING_PAGE_SETTINGS', None):
    app.config.from_envvar('LANDING_PAGE_SETTINGS')
else:
    app.config.from_object('landing_page.default_settings')


if not app.debug:
    import logging
    from logging.handlers import TimedRotatingFileHandler
    # https://docs.python.org/3.6/library/logging.handlers.html#timedrotatingfilehandler
    file_handler = TimedRotatingFileHandler(os.path.join(app.config['LOG_DIR'], 'landing_page.log'), 'midnight')
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(logging.Formatter('<%(asctime)s> <%(levelname)s> %(message)s'))
    app.logger.addHandler(file_handler)

import landing_page.views
