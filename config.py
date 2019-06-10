import os
import json

from utils.directories import PROJECT_ROOT_DIR


class Config(object):

    def __init__(self):
        with open(os.path.join(PROJECT_ROOT_DIR, 'config.json')) as f:
            config = json.load(f)

        self.access_token = config['AccessToken']
        self.refresh_token = config['RefreshToken']
