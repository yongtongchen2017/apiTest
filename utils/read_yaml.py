import yaml

import os

CURRENT_DIR=os.path.dirname(os.path.abspath(__file__))
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

from .logger import logger

def read_yaml(path):
    logger.info("BASE_DIR is: "+BASE_DIR)
    fileDir= BASE_DIR + '/testdata/' + path
    logger.info("fileDir is:" + fileDir)
    with open(fileDir, encoding="utf-8") as f:
        yaml_data = yaml.safe_load(f)
        return yaml_data
