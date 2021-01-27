from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class DriverFactory:
    
    def __init__(self, config):
        self._config = config

    def create(self, name):
        if name == 'chrome':
            return create_chrome_driver
        elif name == 'chrome_remote':
            return create_remote_chrome_driver(self._config)
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

def create_remote_chrome_driver(config):
    host = config['web_driver']['remote']['uri']
    driver = webdriver.Remote(command_executor=f"{host}/wd/hub",options=create_chrome_options())
    return driver
    
def create_firefox_driver():
    raise NotImplementedError
    
def create_remote_firefox_driver():
    raise NotImplementedError