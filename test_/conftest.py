import pytest
import time
from selenium import webdriver
from Library.config import config
from selenium.webdriver.firefox.options import Options




@pytest.fixture(params=["Chrome","Edge","Firefox"])
def _driver(request):
    if request.param == "Chrome":
        driver_obj = webdriver.Chrome(config.Chrome_Driver_Path)

    elif request.param == "Edge":
        driver_obj = webdriver.Edge(config.Edge_Driver_Path)

    elif request.param == "Firefox":
        options = Options()
        options.binary_location = r"C:\Program Files\Mozilla Firefox\firefox.exe"
        driver_obj = webdriver.Firefox(executable_path= config.Firefox_Driver_Path, options=options)


    # path = r'C:\Users\admin\Downloads\chromedriver_win32\chromedriver.exe'
    # driver_obj = webdriver.Chrome(path)

    driver_obj.get(config.URL)
    driver_obj.maximize_window()
    time.sleep(2)
    yield driver_obj
    driver_obj.implicitly_wait(30)
    driver_obj.close()