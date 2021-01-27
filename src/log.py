import logging
import time
import inspect
import sys

def get_logger():
   return logging.getLogger()

# logger format https://docs.python.org/3/library/logging.html
def set_logging_config() -> None:
    logFormatter = logging.Formatter("%(pathname)s %(asctime)s [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("./selenium.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)
