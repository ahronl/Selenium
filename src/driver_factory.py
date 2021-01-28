from selenium import webdriver

class DriverFactory:
    
    def __init__(self, conf):
        self._config = conf

    def create(self, name):
        if name == 'chrome':
            return self.create_chrome_driver()
        elif name == 'chrome_remote':
            return self.create_remote_chrome_driver()
        elif name == 'firefox':
            return self.create_firefox_driver()
        elif name == 'firefox_remote':
            return self.create_remote_firefox_driver()
    
    def create_chrome_options(self):
        chrome_options = webdriver.chrome.options.Options()
        chrome_options.experimental_options["prefs"] = {}
        return chrome_options

    def create_chrome_driver(self):
        chrome_options = self.create_chrome_options()
        return webdriver.Chrome(options=chrome_options)

    def create_remote_chrome_driver(self):
        host = self._config['web_driver']['remote']['uri']
        driver = webdriver.Remote(command_executor=f"{host}/wd/hub",options=self.create_chrome_options())
        return driver
    
    def create_firefox_driver(self):
        raise NotImplementedError
    
    def create_remote_firefox_driver(self):
        raise NotImplementedError