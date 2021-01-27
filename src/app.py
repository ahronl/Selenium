from log import set_logging_config, get_logger
from driver_factory import DriverFactory

def app() -> None:
    
    set_logging_config()

    get_logger().info("starting....")

    driver_factory = DriverFactory()
    driver = driver_factory.create('chrome_remote')
    driver.maximize_window()
    driver.get("https://www.python.org")
    assert "Python" in driver.title

if __name__ == "__main__":
    app()
