from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialize Chrome WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# 1. Open the URL
driver.get("https://magnus.jalatechnologies.com/")

# 2. Print current URL
print("Current URL:", driver.current_url)

# 3. Print page title
print("Page Title:", driver.title)

# 4. Get page source
page_source = driver.page_source
print("Page Source Length:", len(page_source))

# 5. Locate the username field using find_element()
username = driver.find_element(By.ID, "UserName")

# 6. Send input using send_keys()
username.send_keys("training@jalaacademy.com")
print("Entered username.")

# 7. Locate all input fields using find_elements()
all_inputs = driver.find_elements(By.TAG_NAME, "input")
print("Total input fields:", len(all_inputs))

# 8. get_attribute() and get_tag_name()
print("Username Tag Name:", username.tag_name)
print("Username 'type' attribute:", username.get_attribute("type"))

# 9. Check visibility and status
print("Username is displayed:", username.is_displayed())
print("Username is enabled:", username.is_enabled())

# 10. Enter password
driver.find_element(By.ID, "Password").send_keys("jobprogram")

# 11. Get login button and click
login_btn = driver.find_element(By.ID, "btnLogin")
print("Login Button Text:", login_btn.text)
login_btn.click()
print("Clicked login.")

# 12. Pause for 3 seconds
time.sleep(3)

# 13. switch_to (no alert/frame here, just showing usage)
driver.switch_to.default_content()

# 14. manage - get window size and position
print("Window Size:", driver.get_window_size())
print("Window Position:", driver.get_window_position())

# 15. Window handles
print("Current Window Handle:", driver.current_window_handle)
print("All Window Handles:", driver.window_handles)

# 16. Navigate to a different page
driver.get("https://magnus.jalatechnologies.com/Home/Checkbox")
print("Navigated to Checkbox page.")

# 17. Navigate back
driver.back()
print("Navigated back.")
time.sleep(1)

# 18. Navigate forward
driver.forward()
print("Navigated forward.")
time.sleep(1)

# 19. Refresh the page
driver.refresh()
print("Page refreshed.")
time.sleep(1)

# 20. Locate checkboxes and click if not selected
checkboxes = driver.find_elements(By.XPATH, "//input[@type='checkbox']")
print("Total checkboxes found:", len(checkboxes))

for i, box in enumerate(checkboxes):
    if not box.is_selected():
        box.click()
    print(f"Checkbox {i + 1} selected:", box.is_selected())

# 21. Close the browser
driver.quit()
