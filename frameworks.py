import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import logging
import time

# ================== LOGGER SETUP ====================
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# ================== BASE SETUP FIXTURE ====================
@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.maximize_window()
    driver.implicitly_wait(10)
    request.cls.driver = driver
    yield
    driver.quit()

# ================== TEST CLASS ====================
@pytest.mark.usefixtures("setup")
class TestRegistrationAllInOne:

    # ================== PAGE ELEMENTS ====================
    def get_first_name(self):
        return self.driver.find_element(By.NAME, "firstname")

    def get_last_name(self):
        return self.driver.find_element(By.NAME, "lastname")

    def get_email(self):
        return self.driver.find_element(By.NAME, "reg_email__")

    def get_password(self):
        return self.driver.find_element(By.NAME, "reg_passwd__")

    def get_signup_btn(self):
        return self.driver.find_element(By.NAME, "websubmit")

    # ================== PAGE ACTIONS ====================
    def register_user(self, first, last, email, password):
        logging.info(f"Registering user: {first} {last}")
        self.get_first_name().send_keys(first)
        self.get_last_name().send_keys(last)
        self.get_email().send_keys(email)
        self.get_password().send_keys(password)
        time.sleep(1)
        self.get_signup_btn().click()
        time.sleep(2)

    # ================== DATA-DRIVEN TEST ====================
    @pytest.mark.smoke
    @pytest.mark.parametrize("first,last,email,password", [
        ("Kusuma", "Kuppili", "kusuma1@gmail.com", "test1234"),
        ("Harsha", "gurugubelli", "harsha2@gmail.com", "test4567")
    ])
    def test_valid_registration(self, first, last, email, password):
        self.driver.get("https://www.facebook.com/r.php")
        self.register_user(first, last, email, password)
        assert "facebook" in self.driver.title.lower()

    # ================== EMPTY FORM TEST ====================
    @pytest.mark.regression
    def test_empty_form(self):
        self.driver.get("https://www.facebook.com/r.php")
        self.register_user("", "", "", "")
        assert "required" in self.driver.page_source.lower()

    # ================== SKIPPED TEST ====================
    @pytest.mark.skip(reason="This is a skipped test")
    def test_skip_example(self):
        assert False

    # ================== DEPENDENT TESTS ====================
    @pytest.mark.dependency()
    def test_base_test(self):
        logging.info("Running base test...")
        assert True

    @pytest.mark.dependency(depends=["TestRegistrationAllInOne::test_base_test"])
    def test_dependent_case(self):
        logging.info("Running dependent test...")
        assert True

    # ================== INVOCATION COUNT ====================
    @pytest.mark.smoke
    @pytest.mark.parametrize("i", range(3))
    def test_multiple_invocations(self, i):
        logging.info(f"Running invocation #{i+1}")
        self.driver.get("https://www.facebook.com/")
        assert "facebook" in self.driver.title.lower()
