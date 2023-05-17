import logging
import os
import time

BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_PATH = os.path.join(BASE_DIR, "output")
print("LOG_PATH is: ",LOG_PATH)
if not os.path.exists(LOG_PATH):
    os.mkdir(LOG_PATH)


class Logger:
    def __init__(self):
        self._logName = os.path.join(LOG_PATH, "log-{}.log".format(time.strftime("%Y%m%d")))
        self._logger = logging.getLogger("logger")
        self._logger.setLevel(logging.DEBUG)
        self._formatter = logging.Formatter('[%(asctime)s][%(filename)s %(lineno)d][%(levelname)s]:%(message)s')
        self._streamHandler = logging.StreamHandler()
        self._fileHandler = logging.FileHandler(self._logName, mode="a", encoding="utf-8")
        self._streamHandler.setFormatter(self._formatter)
        self._fileHandler.setFormatter(self._formatter)
        self._logger.addHandler(self._streamHandler)
        self._logger.addHandler(self._fileHandler)

    def get_logger(self):
        return self._logger


logger = Logger().get_logger()
