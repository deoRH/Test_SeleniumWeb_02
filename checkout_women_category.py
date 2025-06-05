from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time
import requests
from test_login import login
from selenium.webdriver.common.action_chains import ActionChains

def checkout_women_category (driver):

    wait = WebDriverWait(driver, 10)
    category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="accordian"]/div[1]/div[1]/h4/a')))
    driver.execute_script("arguments[0].scrollIntoView(true);", category)
    time.sleep(1)
    driver.execute_script("arguments[0].click();", category)
    print(category.text)

    element = driver.find_element(By.ID, "Women").click()
    time.sleep(3)

    wait = WebDriverWait(driver, 5)
    sub_category = wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@id="Women"]/div/ul/li[1]/a')))
    print(sub_category.text)
    sub_category.click()

    dress_hover = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/img')
    action = ActionChains (driver)
    action.move_to_element(dress_hover).perform()
    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/a').click()

    wait = WebDriverWait(driver, 5)
    popup_added = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[1]')))
    print(popup_added.text)

    driver.find_element (By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button').click()

    driver.find_element (By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[3]/div/div[2]/ul/li/a').click()

    wait = WebDriverWait(driver, 5)
    stylish_dress = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2')))
    print(stylish_dress.text)

    wait = WebDriverWait(driver, 10)
    quantity_input = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="quantity"]')))
    quantity_input.clear()
    quantity_input.send_keys("3") 
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()

    wait = WebDriverWait(driver, 5)
    popup_added = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[1]')))
    print(popup_added.text) 
    time.sleep(3)
    driver.find_element (By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button').click()
    time.sleep(3)

    review_name = "tester"
    email_address = "mail@mail.com"
    review = "Ini untuk testing saja!"

    review_name_field = driver.find_element(By.XPATH, '//*[@id="name"]')
    email_address_field = driver.find_element(By.XPATH, '//*[@id="email"]')
    review_field = driver.find_element(By.XPATH, '//*[@id="review"]')

    review_name_field.send_keys(review_name)
    print(review_name_field.get_attribute("value"))
    email_address_field.send_keys(email_address)
    print(email_address_field.get_attribute("value"))
    review_field.send_keys(review)
    print(review_field.get_attribute("value"))
    time.sleep(4)

    driver.find_element(By.ID, "button-review").click()
    wait = WebDriverWait(driver, 10)
    success_message = wait.until(
     EC.visibility_of_element_located((By.XPATH, "//*[contains(@class, 'alert-success')]"))
    )
    print(success_message.text)
    time.sleep(2)

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[1]/a').click()
