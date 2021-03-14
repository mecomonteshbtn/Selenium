from selenium import webdriver
import time

with webdriver.Firefox(executable_path='Drivers/geckodriver') as driver:
    # Open a local file
    driver.get('Url_for_your_file.html')
    driver.maximize_window()

    # Close a javascript alert window
    button = driver.find_element_by_id('btn')
    button.click()
    alert = driver.switch_to_alert()
    # Close a dialog window
    alert.dismiss()

    # Close a javascript confirm: It has 2 options or buttons
    button = driver.find_element_by_name('confirm-btn')
    button.click()
    alert = driver.switch_to_alert()
    # Close a dialog window pushing accept button
    alert.accept()  # alert.dismiss()

    # Close a javascript prompt: It requiere to input a value
    button = driver.find_element_by_name('confirm-btn')
    button.click()
    alert = driver.switch_to_alert()
    alert.send_keys('Meco')
    # Close a dialog window pushing accept button
    alert.accept()  # alert.dismiss()
