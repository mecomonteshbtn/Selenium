from selenium import webdriver
import time

# Using your browser driver
url = 'https://www.w3schools.com/howto/howto_html_file_upload_button.asp'
with webdriver.Firefox(executable_path='Drivers/geckodriver') as driver:
    driver.maximize_window()
    driver.get(url)
    upload = driver.find_element_by_id('myFile')
    upload.send_keys('/home/meco/Desktop/Personal Documents/profile.png')
    time.sleep(3)
