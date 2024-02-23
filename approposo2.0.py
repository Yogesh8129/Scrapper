from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def product_info():
    driver = login()
    # Wait for the products page to load
    time.sleep(5)
    whats_new_category(driver)
    data = infinite_scroll(driver)
    get_product_details(data, driver)
    csv_export(data)


def csv_export(data):
    df = pd.DataFrame(data)
    # Save the DataFrame to a CSV file
    df.to_csv("products.csv", index=False)
    print("Products data saved to products.csv")


def get_product_details(data, driver):
    elements = driver.find_elements(By.XPATH, "//div[@class='product-info-card']")
    for element in elements:
        name_element = element.find_element(By.XPATH,
                                            ".//div[contains(@class, 'text-theme_1_grey2') and contains(@class, 'line-clamp-2')]")
        name = name_element.text

        price_element = element.find_element(By.XPATH, ".//span[@class='text-base font-bold smScreen:text-xs']")
        price = price_element.text

        data.append((name, price))
    for name, price in data:
        print(f"Name: {name}, Price: {price}")


def infinite_scroll(driver):
    last_height = driver.execute_script("return document.body.scrollHeight")
    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(2)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    data = []
    time.sleep(5)
    return data


def whats_new_category(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'collection-0-view-all')))
    driver.find_element(By.XPATH, '//*[@id="collection-0-view-all"]/span').click()
    print("inside what's new")
    time.sleep(5)


def login():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://app.roposoclout.com/staff-login")
    driver.maximize_window()
    time.sleep(2)
    driver.find_element(By.ID, "email-input").send_keys("aashi@desertsundesigns.com")
    driver.find_element(By.ID, "login-page-get-otp-button").click()
    time.sleep(2)
    driver.find_element(By.ID, "password-input").send_keys("hTm[aCoWYwKL!1")
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'login-page-proceed-button')))
    driver.find_element(By.ID, "login-page-proceed-button").click()
    print("login successful")
    return driver


product_info()
