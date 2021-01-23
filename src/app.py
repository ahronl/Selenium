from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def make_chrome_options() -> None:
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_prefs = {}
    chrome_options.experimental_options["prefs"] = chrome_prefs
    chrome_prefs["profile.default_content_settings"] = {"images": 2}
    return chrome_options

def app() -> None:
    chrome_options = make_chrome_options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("http://www.python.org")
    assert "Python" in driver.title

if __name__ == "__main__":
    app()
