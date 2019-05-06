import os
from configparser import ConfigParser

from strava_reader.utils.directories import PROJECT_ROOT_DIR

class Config(object):

    def __init__(self):
        config = ConfigParser()
        config.read(os.path.join(PROJECT_ROOT_DIR, 'config.ini'))
        self.client_secret =
        self.AccessToken
        self.RefreshToken

