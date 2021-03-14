from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

# Using your browser driver
url = 'https://www.w3schools.com/howto/howto_custom_select.asp'
with webdriver.Firefox(executable_path='Drivers/geckodriver') as driver:
    driver.maximize_window()
    driver.get(url)

    menu = Select(driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/select'))
    menu.select_by_index(11)
    menu.select_by_value('6')
    menu.select_by_visible_text('Ford')
    
    # NOTICE: elements is in plural
    dropdown = driver.find_element_by_xpath('/html/body/div[6]/div[1]/div[1]/div[3]/div[1]/select')
    options = driver.find_elements_by_tag_name('option')
    for option in options:
        option.click()