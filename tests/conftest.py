import pytest
from selene.support.shared import browser


@pytest.fixture(scope="module", autouse=True)
def open_browser():
    browser.config.base_url = 'https://demoqa.com'
    browser.driver.maximize_window()

    yield

    browser.quit()