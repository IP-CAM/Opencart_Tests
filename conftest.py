import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox", help="choose your browser")
    parser.addoption("--url", action="store", default="https:localhost/admin/", help="choose your browser")


@pytest.fixture
def browser(request):
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    else:
        raise Exception(f"{browser} is not supported!")

    driver.maximize_window()
    driver.get(request.config.getoption("--url"))
    request.addfinalizer(driver.quit)

    return driver


