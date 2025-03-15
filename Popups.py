from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open page with alerts
driver.get("https://demo.automationtesting.in/Alerts.html")
time.sleep(2)

# 2. Handle simple alert
driver.find_element(By.XPATH, "//button[contains(text(),'alert box')]").click()
time.sleep(1)

# Immediately handle the alert
alert = driver.switch_to.alert
print("Alert Message:", alert.text)
alert.accept()  # Close alert before proceeding

# 3. Prompt Alert with text
driver.find_element(By.XPATH, "//a[text()='Alert with Textbox']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'prompt box')]").click()
time.sleep(1)

prompt_alert = driver.switch_to.alert
print("Prompt Alert:", prompt_alert.text)
prompt_alert.send_keys("Selenium Test")
prompt_alert.accept()

# 4. Confirmation Alert
driver.find_element(By.XPATH, "//a[text()='Alert with OK & Cancel ']").click()
driver.find_element(By.XPATH, "//button[contains(text(),'confirm box')]").click()
time.sleep(1)

confirm_alert = driver.switch_to.alert
print("Confirm Alert:", confirm_alert.text)
confirm_alert.dismiss()  # Press Cancel

# 5. Handle single window
single_window = driver.current_window_handle
print("Current window:", single_window)

# 6. Handle multiple windows
driver.get("https://demo.automationtesting.in/Windows.html")
driver.find_element(By.XPATH, "//a[text()='Open New Seperate Windows']").click()
driver.find_element(By.XPATH, "//button[@onclick='newwindow()']").click()
time.sleep(2)

all_windows = driver.window_handles
print("All windows:", all_windows)

for handle in all_windows:
    if handle != single_window:
        driver.switch_to.window(handle)
        print("Switched to:", driver.title)
        driver.close()

driver.switch_to.window(single_window)

# 7. Switch to frame
driver.get("https://demo.automationtesting.in/Frames.html")
frame = driver.find_element(By.ID, "singleframe")
driver.switch_to.frame(frame)
driver.find_element(By.TAG_NAME, "input").send_keys("Inside frame")
driver.switch_to.default_content()
print("Entered text inside frame.")

# 8. Popup Alert from demoqa
driver.get("https://demoqa.com/alerts")
time.sleep(2)
driver.find_element(By.ID, "alertButton").click()
time.sleep(1)
popup = driver.switch_to.alert
print("Popup Text:", popup.text)
popup.accept()

# Done
driver.quit()
