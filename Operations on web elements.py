from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Setup Chrome
driver = webdriver.Chrome()
driver.maximize_window()

# Step 1: Open the website
driver.get("https://magnus.jalatechnologies.com/")

try:
    # Step 2: Wait for the username input to appear
    username_field = WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "UserName"))
    )
    username_field.send_keys("training@jalaacademy.com")
    print("Entered username.")

    # Step 3: Fill password
    driver.find_element(By.ID, "Password").send_keys("jobprogram")

    # Step 4: Click login button
    driver.find_element(By.ID, "btnLogin").click()
    print("Login clicked.")

    # Step 5: Wait for homepage to load
    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.ID, "MenusDashboard"))
    )
    print("Logged in successfully.")

    # Step 6: Go to Radio Button page
    driver.get("https://magnus.jalatechnologies.com/Home/RadioButton")

    # Wait for page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "body")))

    # Step 7: Try to click Java radio button
    try:
        java_label = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//label[contains(text(),'Java')]"))
        )
        java_label.click()
        print(" Java radio button clicked.")
    except Exception as e:
        print(" Java radio button not found:", e)

    # Step 8: Check all radio buttons
    radio_buttons = driver.find_elements(By.XPATH, "//input[@type='radio']")
    print("Total radio buttons found:", len(radio_buttons))

    for i, btn in enumerate(radio_buttons):
        print(f"Radio Button {i+1}: Value: {btn.get_attribute('value')}, Selected: {btn.is_selected()}")

except Exception as e:
    print("⚠️ Error occurred:", e)

# Wait to observe the result before closing
time.sleep(3)
driver.quit()
