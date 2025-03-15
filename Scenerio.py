from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import time
import requests

# Setup driver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# 1. Capture Screenshot
driver.get("https://demo.guru99.com/test/newtours/")
driver.save_screenshot("homepage_screenshot.png")

# 2. Click element in iFrame
driver.get("https://demo.automationtesting.in/Frames.html")
driver.switch_to.frame(driver.find_element(By.ID, "singleframe"))
driver.find_element(By.TAG_NAME, "input").send_keys("Hello Frame")
driver.switch_to.default_content()

# 3. Broken Links
driver.get("https://demo.guru99.com/test/newtours/")
all_links = driver.find_elements(By.TAG_NAME, "a")
for link in all_links:
    url = link.get_attribute("href")
    if url and "http" in url:
        try:
            res = requests.head(url, timeout=5)
            if res.status_code >= 400:
                print(f"Broken Link: {url} | Status: {res.status_code}")
        except:
            print(f"Error accessing: {url}")

# 4. Implicit and Explicit Wait
driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.find_element(By.TAG_NAME, "button").click()
wait = WebDriverWait(driver, 15)
element = wait.until(EC.presence_of_element_located((By.ID, "finish")))
print("Explicit Wait Output:", element.text)

# 5. Action Class
driver.get("https://demo.guru99.com/test/newtours/")
action = ActionChains(driver)
home = driver.find_element(By.LINK_TEXT, "Home")
action.move_to_element(home).perform()  # Hover
action.double_click(home).perform()     # Double Click
action.click_and_hold(home).perform()   # Click and Hold
action.release().perform()

# 6. Web Table Operations
driver.get("https://demo.guru99.com/test/web-table-element.php")
rows = driver.find_elements(By.XPATH, "//table[@class='dataTable']//tr")
print("Total Rows:", len(rows))
cell_data = driver.find_element(By.XPATH, "//table[@class='dataTable']//tr[3]/td[2]").text
print("Data in [3,2]:", cell_data)

# 7. Handling Ajax Auto Suggestions
driver.get("https://www.google.com/")
search = driver.find_element(By.NAME, "q")
search.send_keys("Selenium WebDriver")
time.sleep(2)
suggestions = driver.find_elements(By.XPATH, "//ul[@role='listbox']//li")
for s in suggestions:
    if "selenium webdriver python" in s.text.lower():
        s.click()
        break

# 8. Select a Date from Calendar
driver.get("https://demo.automationtesting.in/Datepicker.html")
driver.find_element(By.ID, "datepicker1").send_keys("03/15/2025")
driver.find_element(By.ID, "datepicker1").send_keys(Keys.ENTER)

# 9. Cookies Operations
driver.get("https://www.google.com/")
driver.add_cookie({"name": "MyCookie", "value": "123456"})
print("Cookie Added:", driver.get_cookies())
driver.delete_cookie("MyCookie")
print("After Deletion:", driver.get_cookies())

# Close the browser
driver.quit()
