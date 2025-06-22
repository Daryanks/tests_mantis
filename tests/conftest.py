import pytest
from fixture.application import Application
import json
import os.path

fixture=None
target=None

def load_config(file):
    global target
    if target is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), file)
        with open(config_file) as f:
            target = json.load(f)
    return target


@pytest.fixture(autouse=True)
def config(request):
    return load_config(request.config.getoption("--target"))

@pytest.fixture(autouse=True)
def app(request, config):
    global fixture
    browser = request.config.getoption("--browser")
    if fixture is None or not fixture.is_valid:
        fixture = Application(browser=browser, config=config)
    fixture.session.login(config['webadmin']['username'], config['webadmin']['password'])
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        #fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption("--target", action="store", default="target.json")

