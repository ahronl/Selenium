from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

import logging

def make_chrome_options() -> None:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def set_logging_config() -> None:

    logFormatter = logging.Formatter("%(asctime)s [%(threadName)-12.12s] [%(levelname)-5.5s]  %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.DEBUG)

    fileHandler = logging.FileHandler("./selenium.log")
    fileHandler.setFormatter(logFormatter)
    rootLogger.addHandler(fileHandler)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(logFormatter)
    rootLogger.addHandler(consoleHandler)

def print_logs_example() -> None:
    logging.getLogger().debug("Debug message")
    logging.getLogger().info("Informative message")
    logging.getLogger().error("Error message")

def make_driver():
    chrome_options = make_chrome_options()
    return webdriver.Chrome(options=chrome_options)

def app() -> None:
    set_logging_config()
    print_logs_example()

    driver = make_driver()
    driver.get("http://www.python.org")
    assert "Python" in driver.title

if __name__ == "__main__":
    app()
