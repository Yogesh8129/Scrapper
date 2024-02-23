from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

website = 'https://www.adamchoi.co.uk/overs/detailed'

driver = webdriver.Chrome()
driver.get(website)
