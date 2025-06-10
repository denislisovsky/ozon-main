from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import pytest
import time

@pytest.fixture
def driver():
    service = Service()
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

def test_open_wildberries_main_page(driver):
    driver.get("https://regem.store/")
    time.sleep(3)

    assert "Украшения из натуральных камней и минералов REGEM" in driver.title 
    assert "regem.store" in driver.current_url
