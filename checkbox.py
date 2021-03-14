from selenium import webdriver
import time

# Using your browser driver
url = 'https://www.w3schools.com/howto/howto_css_custom_checkbox.asp'
with webdriver.Firefox(executable_path='Drivers/geckodriver') as driver:
    driver.maximize_window()
    driver.get(url)
    checkbox = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/input[1]')
    print('checkbox one')
    print(checkbox.is_selected())
    print(checkbox.is_enabled())
    print(checkbox.is_displayed())

    checkbox = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/input[2]')
    print('checkbox two')
    print(checkbox.is_selected())
    print(checkbox.is_enabled())
    print(checkbox.is_displayed())

    # NOTICE: elements is in plural
    checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
    for checkbox in checkboxes:
        if checkbox.is_displayed() is True and checkbox.is_selected() is False:
            checkbox.click()
