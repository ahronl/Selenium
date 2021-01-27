from log import set_logging_config, get_logger
from driver_factory import DriverFactory
from pathlib import Path

import yaml

def read_conf():
    path = (Path(__file__).parent / "../etc/config.yml").resolve()
    with open(path) as file:
        conf = yaml.load(file, Loader=yaml.FullLoader)
        return conf

def app() -> None:
    set_logging_config()
    get_logger().info("starting....")

    config = read_conf()
    driver_factory = DriverFactory(config)
    driver = driver_factory.create('chrome_remote')
    driver.maximize_window()
    driver.get("https://www.python.org")
    assert "Python" in driver.title

if __name__ == "__main__":
    app()
