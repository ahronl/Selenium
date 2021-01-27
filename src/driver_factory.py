from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DriverFactory:
    def create(self, name):
        if name == 'chrome':
            return create_chrome_driver
        elif name == 'chrome_remote':
            return create_remote_chrome_driver()
        elif name == 'firefox':
            return create_firefox_driver()
        elif name == 'firefox_remote':
            return create_remote_firefox_driver()


def create_chrome_options() -> None:
    chrome_options = webdriver.chrome.options.Options()
    chrome_options.experimental_options["prefs"] = {}
    return chrome_options

def create_chrome_driver():
    chrome_options = create_chrome_options()
    return webdriver.Chrome(options=chrome_options)

def create_remote_chrome_driver():
    driver = webdriver.Remote(command_executor='http://host.docker.internal:4444/wd/hub',options=create_chrome_options())
    return driver

def create_firefox_driver():
    raise NotImplementedError

def create_remote_firefox_driver():
    raise NotImplementedError