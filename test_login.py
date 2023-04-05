import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# selenium -> pip install selenium / 

class OpenCartRegisztracioTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./TestProjects/chromedriver.exe") # chromedriver szükséges
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_bejelentkezes_oldal_megjelenes(self):
        driver = self.driver
        driver.get("https://demo.opencart.com")
        my_acc_dropdown = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(), 'My Account')]")))
        my_acc_dropdown.click()

        login_option = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Login']")))
        login_option.click()

        # teszt hogy a URL tartalmazza a route-ot
        self.assertIn("https://demo.opencart.com/index.php?route=account/login", driver.current_url)
        # teszt: login oldal cime egyezik
        self.assertEqual("Account Login", driver.title)
    
    def test_bejelentkezes(self):
        driver = self.driver
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        form = driver.find_element(By.ID, "form-login")
        
        # teszt: megjeleniti-e a login formot
        self.assertTrue(form.is_displayed)

        driver.find_element(By.NAME, "email").send_keys("validemail@email.com")
        driver.find_element(By.NAME, "password").send_keys("titkosjelszo123")

        driver.find_element(By.XPATH, "//button[@type='submit']").click()

        account_menu = driver.find_element(By.XPATH, "//span[contains(text(), 'My Account')]")
        
        # teszt: majd a belépés után megjelenik-e az account menü
        self.assertTrue(account_menu.is_displayed)

    def test_elfelejtett_jelszo(self):
        driver = self.driver
        driver.get("https://demo.opencart.com/index.php?route=account/login")
        elf_jelszo_link = driver.find_element(By.XPATH, "(//a[text() = 'Forgotten Password'])[1]")
        elf_jelszo_link.click()

        elf_jelszo_form = driver.find_element(By.ID, "form-forgotten")

        # teszt: elfelejtett jelszo form megjelenik-e
        self.assertTrue(elf_jelszo_form.is_displayed)
        # teszt: a URL tartalmazza a megfelelő route-ot
        self.assertIn("https://demo.opencart.com/index.php?route=account/forgotten", driver.current_url)
        # teszt: a cim egyezik-e az elfelejtett oldal cimevel
        self.assertEqual("Forgot Your Password?", driver.title)

    def tearDown(self):
        self.driver.close()
    
# unittestek futtatása

if __name__ == "__main__":
    unittest.main()