import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

# Run typing: python3 -m unittest discover
# Run typing: python3 test_SEREMPRE.py
class TermsConditions(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox(executable_path='Drivers/geckodriver')
        driver = self.driver
        driver.maximize_window()
        driver.get('https://co-tc-shopper-web-stage.serempre.dev/')
        driver.implicitly_wait(3)

    def test_check_terms(self):
        driver = self.driver
        city = driver.find_element_by_id("react-select-2-input")
        city.send_keys("Bogota", Keys.ENTER)
        button_continue = driver.find_element_by_class_name("sc-jSFkmK")
        button_continue.click()
        driver.implicitly_wait(3)

        button_consumer = driver.find_element_by_class_name("sc-jSFkmK")
        button_consumer.click()

        # Probar que el codigo de area sea el correcto con un assersion
        phone = driver.find_element_by_name("abi-phone")
        phone.send_keys("3006259575")
        button_join = driver.find_element_by_class_name("sc-jSFkmK")
        button_join.click()
        driver.implicitly_wait(3)

        checkbox_terms = driver.find_element_by_name('abi-checkbox-terms')
        if checkbox_terms.is_displayed() is True and checkbox_terms.is_selected() is False:
            checkbox_terms.click()
        checkbox_policies = driver.find_element_by_name('abi-checkbox-policies')
        if checkbox_policies.is_displayed() is True and checkbox_policies.is_selected() is False:
            checkbox_policies.click()
        button_continue = driver.find_element_by_class_name('sc-jSFkmK')
        button_continue.click()
        driver.implicitly_wait(3)

        # Fill the form with first name, last name, and email
        first_name = driver.find_element_by_id('register-name')
        first_name.send_keys('Candy')
        last_name = driver.find_element_by_id('register-lastName')
        last_name.send_keys('Montes')
        email = driver.find_element_by_id('register-email')
        email.send_keys('candymontes@gmail.com')
        button_next = driver.find_element_by_class_name('sc-jSFkmK')
        button_next.click()
        time.sleep(3)

        # Input the address Cra. 13 #96-67
        address = driver.find_element_by_id('address')
        address.send_keys('Cra. 13 #96-67')
        driver.implicitly_wait(5)
        nearest_location = driver.find_element_by_class_name('sc-cBoprd')
        nearest_location.click()
        driver.implicitly_wait(5)
        button_select_location = driver.find_element_by_class_name('sc-jSFkmK')
        button_select_location.click()
        driver.implicitly_wait(3)

        # Validation text
        validated = driver.find_element_by_class_name('sc-carGAA')
        self.assertEqual(validated.text, '¡Te has validado exitosamente!')
        driver.close()

    def tearDown(self):
        self.driver.implicitly_wait(3)
        driver.quit()


if __name__ == "__main__":
    unittest.main(verbosity=2)