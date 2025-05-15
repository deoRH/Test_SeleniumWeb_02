from selenium import webdriver #driver untuk website
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

def checkout_men_category (driver):

    element = driver.find_element(By.XPATH, '/html/body/section[2]/div/div/div[1]/div/div[3]/div/ul/li[2]/a')
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)
    print(element.text)
    time.sleep(3)

    time.sleep(3)
    wait = WebDriverWait(driver, 20)
    hm_link = wait.until(EC.element_to_be_clickable((
     By.XPATH, "//a[contains(@href, '/brand_products/H&M')]"
    )))
    hm_link.click()

    mentshirt_hover = driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[1]/div[1]/img')
    action = ActionChains (driver)
    action.move_to_element(mentshirt_hover).perform()
    time.sleep(2)

    driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/div/a').click()
    time.sleep(10)
    wait = WebDriverWait(driver, 10)
    popup_added = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[1]')))
    print(popup_added.text)

    driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button').click()
    driver.find_element(By.XPATH, '/html/body/section/div/div[2]/div[2]/div/div[6]/div/div[2]/ul/li/a').click()

    wait = WebDriverWait(driver, 5)
    regular_fit = wait.until(EC.visibility_of_element_located((By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/h2')))
    print(regular_fit.text)
    time.sleep(3)

    driver.find_element(By.XPATH, '/html/body/section/div/div/div[2]/div[2]/div[2]/div/span/button').click()
    wait = WebDriverWait(driver, 10)
    popup_added = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cartModal"]/div/div/div[2]/p[1]')))
    print(popup_added.text)
    driver.find_element(By.XPATH, '//*[@id="cartModal"]/div/div/div[3]/button').click()


