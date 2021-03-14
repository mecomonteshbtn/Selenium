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
    # Follow the link: Forgot Password
    link = driver.find_element_by_link_text('Forgot Password')
    # Follow the link using a partial link
    # link = driver.find_element_by_partial_link_text('Forgot')
    # link = driver.find_element_by_partial_link_text('Password')
    # Click on the link
    link.click()
    # Access to a component of the web app
    user = driver.find_element_by_name('form-element--1')
    # send the email for this component
    user.send_keys('helloworl@gmail.com')
    # click on captcha
    validate = driver.find_element_by_class_name('recaptcha-checkbox-border')
    validate.click()
    # Click on the buttom
    button = driver.find_element_by_class_name('btn-primary')
    button.click()
    time.sleep(5)

    # Close the browser
    # driver.close()
