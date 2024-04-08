from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_collection_info(collection_name):
    driver = login()
    # Wait for the products page to load
    time.sleep(5)
    collection_details(driver, collection_name)
    data = infinite_scroll(driver)
    get_product_details(data, driver)
    csv_export(data, collection_name)

def get_collections_info(collection_count):
    driver = login()
    # Wait for the products page to load
    time.sleep(5)
    print("before foreach")
    for collection_number in range(collection_count):
        print("inside foreach")
        collection_name = 'collection-' + str(collection_number) + '-view-all'
        print(collection_name)
        collection_details(driver, collection_name)
        data = infinite_scroll(driver)
        category_name = get_product_details(data, driver)
        print(category_name)
        csv_export(data, category_name)
        driver.back()

def csv_export(data, category_name):
    df = pd.DataFrame(data)
    # Save the DataFrame to a CSV file
    csv_name = category_name + '.csv'
    df.to_csv(csv_name, index=False)
    print("Products data saved to " + csv_name)

def get_product_details(data, driver):
    category_name = driver.find_element(By.XPATH, "//div[@class='font-bold text-[24px] smScreen:text-sm']").text
    elements = driver.find_elements(By.XPATH, "//div[@class='product-info-card']")
    for element in elements:
        name_element = element.find_element(By.XPATH, ".//div[contains(@class, 'text-theme_1_grey2') and contains(@class, 'line-clamp-2')]")
        name = name_element.text

        price_element = element.find_element(By.XPATH, ".//span[@class='text-base font-bold smScreen:text-xs']")
        price = price_element.text

        data.append((name, price))
    for name, price in data:
        print(f"Name: {name}, Price: {price}")
    return category_name

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


def collection_details(driver, collection):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, collection)))
    collection_xpath = '//*[@id="' + collection + '"]/span'
    print(collection_xpath)
    driver.find_element(By.XPATH, collection_xpath).click()
    print("inside " + collection)
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

# get_collection_info("collection-1-view-all")
# get_collection_info("collection-2-view-all")
# get_collection_info("collection-3-view-all")
# get_collection_info("collection-4-view-all")
# get_collection_info("collection-5-view-all")
# get_collection_info("collection-6-view-all")
# get_collection_info("collection-7-view-all")
# get_collection_info("collection-8-view-all")
# get_collection_info("collection-9-view-all")
# get_collection_info("collection-10-view-all")
# get_collection_info("collection-11-view-all")
# get_collection_info("collection-12-view-all")
# get_collection_info("collection-13-view-all")
# get_collection_info("collection-14-view-all")
# get_collection_info("collection-15-view-all")
# get_collection_info("collection-16-view-all")
# get_collection_info("collection-17-view-all")
# get_collection_info("collection-18-view-all")
# get_collection_info("collection-19-view-all")
# get_collection_info("collection-20-view-all")

get_collections_info(20)



# //*[@id="collection-0-view-all"]/span
