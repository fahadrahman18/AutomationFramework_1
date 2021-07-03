import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g. chrome r firefox")

@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver

    browser = request.config.getoption("--browser")

    if browser == 'chrome':
        driver = webdriver.Chrome(executable_path="C:/Users/User/PycharmProjects/pythonProject/AutomationFramework_1/drivers/chromedriver.exe")
    else:
        pass
    driver.implicitly_wait(10)
    driver.maximize_window()
    request.cls.driver = driver
    yield
    driver.close()
    driver.quit()
    print("Test Completed")