import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class OpenKartRegisztracioTeszt(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./TestProjects/chromedriver.exe")
        
        self.driver.implicitly_wait(10)
    
    def test_regisztracio_oldal_megjelenites(self):

        driver = self.driver
        driver.get("https://demo.opencart.com")
        dropdown_my_acc = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[text() = 'My Account']")))
        dropdown_my_acc.click()

        register_menu_pont = driver.find_element(By.XPATH, "//a[text() = 'Register']")
        register_menu_pont.click()

        self.assertIn("https://demo.opencart.com/index.php?route=account/register", driver.current_url)
        self.assertEqual("Register Account", driver.title)

        register_form = driver.find_element(By.ID, "form-register")
        self.assertTrue(register_form.is_displayed)
    
    def test_regisztracio_helyes(self):
        first_name = "Istvan"
        last_name = "Kovacs"
        email = "kovacsistvan@gmail.com"
        password = "12345"
        news_letter_sub = True

        driver = self.driver


        driver.get("https://demo.opencart.com/index.php?route=account/register")
        driver.find_element(By.ID, "input-firstname").send_keys(first_name)
        driver.find_element(By.ID, "input-lastname").send_keys(last_name)
        driver.find_element(By.ID, "input-email").send_keys(email)
        driver.find_element(By.ID, "input-password").send_keys(password)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if(news_letter_sub):
            driver.find_element(By.ID, "input-newsletter-yes").click()
        else:
            driver.find_element(By.ID, "input-newsletter-no").click
        
        driver.find_element(By.XPATH, "//input[@name='agree']").click()
        driver.find_element(By.XPATH, "//button[text() = 'Continue']").click()
        felh_mezo_ures = driver.find_element(By.ID, "input-firstname").text
        self.assertTrue(driver.find_element(By.XPATH, "//span[text() = 'My Account']").is_displayed)
        self.assertEqual("", felh_mezo_ures)
    
    def test_regisztracio_helytelen_email(self):
        first_name = "Istvan"
        last_name = "Kovacs"
        email = "kovacsistvan"
        password = "12345"
        news_letter_sub = True

        driver = self.driver
        
        driver.get("https://demo.opencart.com/index.php?route=account/register")
        driver.find_element(By.ID, "input-firstname").send_keys(first_name)
        driver.find_element(By.ID, "input-lastname").send_keys(last_name)
        driver.find_element(By.ID, "input-email").send_keys(email)
        driver.find_element(By.ID, "input-password").send_keys(password)
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)
        if(news_letter_sub):
            driver.find_element(By.ID, "input-newsletter-yes").click()
        else:
            driver.find_element(By.ID, "input-newsletter-no").click
        
        driver.find_element(By.XPATH, "//input[@name='agree']").click
        
        self.assertTrue(driver.find_element(By.ID, "error-email").is_displayed)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
