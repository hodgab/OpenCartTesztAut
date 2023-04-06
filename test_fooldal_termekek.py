import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
import time

class FooldalTermekekHozzaadasaTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("./TestProjects/chromedriver.exe")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
    
    def test_termek_hozzaadas(self):
        driver = self.driver
        driver.get("https://demo.opencart.com")
        featured_product_scroll = driver.find_element(By.XPATH, "(//div[@class='content'])[1]")


        driver.execute_script("arguments[0].scrollIntoView();", featured_product_scroll)
        featured_products = driver.find_elements(By.XPATH, "//div[@class='product-thumb']")
        product_quantity = len(featured_products)

        self.assertEqual(4, product_quantity)
        
        for product in featured_products:
            WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//button[@aria-label='Add to Cart']")))
            cart_btn = product.find_element(By.XPATH, "//button[@aria-label='Add to Cart']")
            cart_btn.click()
            succes_popup = product.find_element(By.XPATH, "//div[@class='alert alert-success alert-dismissible']").is_displayed
            self.assertTrue(succes_popup)
    
    

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
