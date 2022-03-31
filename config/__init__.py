from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def browser():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager(log_level=0).install()))

    # Configurations
    driver.maximize_window()

    return driver
