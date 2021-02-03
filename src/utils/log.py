import logging
import time
import inspect
import sys

from pathlib import Path

def get_logger(name):
   return logging.getLogger(name)

# logger format https://docs.python.org/3/library/logging.html
def set_logging_config():
    logFormatter = logging.Formatter("%(pathname)s %(asctime)s [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    log_filer = (Path(__file__).parent / "../../selenium.log").resolve()
    fileHandler = logging.FileHandler(log_filer)
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
