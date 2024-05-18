from datetime import datetime
import sys

from monit import config
from monit import func
from monit.http import HTTPClient

INIT_TIME = datetime.now()


class Monitor:

    @staticmethod
    def register(error=None):
        data = func.build_json(error, INIT_TIME)
        HTTPClient.request(config.handler_url, data)

    @staticmethod
    def end():
        Monitor().register()

    @staticmethod
    def msg(msg):
        data = func.build_json()
        data["custom_msg"] = msg
        HTTPClient.request(config.handler_url, data)

    @staticmethod
    def notify(error=None):
        Monitor().register(error)

    @staticmethod
    def notify_and_exit(error=None):
        Monitor().register(error)
        sys.exit(1)
