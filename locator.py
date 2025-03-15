from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Firefox()
driver.get("https://example.com")  # test page
print("Title is:", driver.title)
time.sleep(3)
driver.quit()
