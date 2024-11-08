from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os

os.environ['OTEL_TRACES_EXPORTER'] = 'none'


def test_app_loads_correctly():
    APP_HOST = os.environ.get("APP_HOST", "app")
    APP_PORT = os.environ.get("APP_PORT", "5000")

    app_url = f"http://{APP_HOST}:{APP_PORT}"
    print(f"\nAttempting to access: {app_url}")

    chrome_options = Options()
    chrome_options.add_argument('--disable-features=ChromeWhatsNewUI')
    chrome_options.add_argument('--disable-domain-reliability')
    chrome_options.add_argument('--disable-logging')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-web-security')
    chrome_options.add_argument('--allow-running-insecure-content')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')
    chrome_options.add_argument('--disable-features=Upgrade-Insecure-Requests')

    driver = webdriver.Remote(
        command_executor=os.environ['SELENIUM_REMOTE_URL'],
        options=chrome_options
    )

    try:
        print("Starting page get...")
        driver.get(app_url)
        print("Get completed")

        print("Waiting for the body element...")
        driver.implicitly_wait(5)
        body = driver.find_element(By.TAG_NAME, "body")
        print(f"Body found. Full text:\n{body.text}")

        print("Verifying 'very simple' text...")
        assert "very simple" in body.text, f"'very simple' text not found. Current text: {body.text}"
        print("Test completed successfully")

    except Exception as e:
        print(f"Error during the test: {str(e)}")
        print(f"Current URL: {driver.current_url}")
        print(f"Page title: {driver.title}")
        print("Page source:")
        print(driver.page_source)
        raise

    finally:
        driver.quit()
