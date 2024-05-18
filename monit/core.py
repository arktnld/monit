from datetime import datetime
import sys

from monit import config
from monit import func
from monit.http import HTTPClient

INIT_TIME = datetime.now()


class Monitor:

    @staticmethod
    def register(error=None, custom_msg=None):
        json = func.build_json(custom_msg, error, INIT_TIME)
        HTTPClient.request(config.handler_url, json)

    @staticmethod
    def end():
        Monitor().register()

    @staticmethod
    def msg(msg):
        Monitor().register(custom_msg=msg)

    @staticmethod
    def notify(error=None, custom_msg=None):
        Monitor().register(error, custom_msg)

    @staticmethod
    def notify_and_exit(error=None, custom_msg=None):
        Monitor().register(error, custom_msg)
        sys.exit(1)
