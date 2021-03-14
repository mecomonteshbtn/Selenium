from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Using your browser driver
url = 'https://www.google.com.co'
url1 = 'https://www.udemy.com/'
url2 = 'https://www.facebook.com'
with webdriver.Firefox(executable_path='Drivers/geckodriver') as driver:
    driver.maximize_window()
    driver.get(url)

    # Go to Udemy, and next to facebook
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[1])
    driver.get(url1)
    driver.get(url2)

    # Go to Google, and next to Facebook
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[2])
    driver.get(url)
    driver.get(url2)

    # Move to tab 1, and go to previous web: from Facebook to Udemy
    driver.switch_to.window(driver.window_handles[1])
    driver.back()

    # Move to tab 0, close tab 0 and tab 1 and move from Udemy to Facebook
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.close()
    driver.switch_to.window(driver.window_handles[0])
    driver.back()
    driver.forward()
