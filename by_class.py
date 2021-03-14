from selenium import webdriver
import time

# Using your browser driver
url = 'https://www.udemy.com/join/login-popup/?locale=en_US&response_type=html&next=https%3A%2F%2Fwww.udemy.com%2Flogout%2F'
with webdriver.Firefox(executable_path='Drivers/geckodriver') as driver:
    # Open the browser
    driver.maximize_window()
    # GET method for the url to test
    driver.get(url)
    # Time.sleep(1) is just to wait for 1 second
    time.sleep(1)
    # Access to a component of the web app
    user = driver.find_element_by_class_name('form-control')
    # send the email for this component
    user.send_keys('mecomontes@gmail.com')
    passwd = driver.find_element_by_class_name('textinput')
    passwd.send_keys('meco002762')
    # Click on the buttom
    button = driver.find_element_by_class_name('btn')
    button.click()
    time.sleep(5)

    # Close the browser
    # driver.close()
