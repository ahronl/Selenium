import logging
import logging.handlers

def setup_config() -> None:
  logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(levelname)s %(message)s')

def get_logger(name="root"):
  logging.getLogger(name)