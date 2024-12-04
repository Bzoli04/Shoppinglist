from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest


# Fixture a Selenium WebDriver elindításához
@pytest.fixture
def browser():
    driver = webdriver.Chrome()  # Ha nincs PATH-ban, add meg a teljes elérési utat: webdriver.Chrome(executable_path="/path/to/chromedriver")
    driver.get("http://127.0.0.1:5000/")  # Flask app URL-je
    yield driver
    driver.quit()


def test_ui_add_item(browser):
    # Keresd meg az input mezőt és a gombot
    input_field = browser.find_element(By.NAME, "item")
    add_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Add')]")

    # Adj hozzá egy elemet
    input_field.send_keys("Milk")
    add_button.click()

    # Ellenőrizd, hogy az elem megjelent a listában
    time.sleep(1)  # Várjunk, hogy a frissítés megtörténjen
    list_items = browser.find_elements(By.TAG_NAME, "li")
    assert any("Milk" in item.text for item in list_items), "Milk was not added to the list!"


def test_ui_delete_item(browser):
    # Adjunk hozzá egy elemet először
    input_field = browser.find_element(By.NAME, "item")
    add_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Add')]")
    input_field.send_keys("Bread")
    add_button.click()

    # Töröljük az elemet
    time.sleep(1)
    delete_button = browser.find_element(By.XPATH, "//li[contains(., 'Bread')]/a[contains(text(), 'Delete')]")
    delete_button.click()

    # Ellenőrizzük, hogy az elem törlődött
    time.sleep(1)
    list_items = browser.find_elements(By.TAG_NAME, "li")
    assert all("Bread" not in item.text for item in list_items), "Bread was not deleted from the list!"


def test_ui_add_multiple_items(browser):
    # Több elem hozzáadása
    items = ["Apple", "Banana", "Orange"]
    input_field = browser.find_element(By.NAME, "item")
    add_button = browser.find_element(By.XPATH, "//button[contains(text(), 'Add')]")

    for item in items:
        input_field.send_keys(item)
        add_button.click()
        time.sleep(1)

    # Ellenőrizd, hogy minden elem hozzá lett adva
    list_items = browser.find_elements(By.TAG_NAME, "li")
    for item in items:
        assert any(item in list_item.text for list_item in list_items), f"{item} was not added to the list!"
