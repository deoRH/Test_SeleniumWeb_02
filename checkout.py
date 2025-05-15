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


def checkout(driver):

    driver.find_element(By.XPATH, '//*[@id="header"]/div/div/div/div[2]/div/ul/li[3]/a').click()
    time.sleep(5)

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'cart_info_table')))
    rows = driver.find_elements(By.XPATH, "//table[@id='cart_info_table']/tbody/tr")
    print("Order Item:")
    for row in rows:
        try:
            product_name = row.find_element(By.XPATH, ".//td[2]/h4/a").text
            price = row.find_element(By.XPATH, ".//td[3]/p").text 
            quantity = row.find_element(By.XPATH, ".//td[4]/button").text
            total = row.find_element(By.XPATH, ".//td[5]/p").text

            print(f"- {product_name} | Harga: {price} | Qty: {quantity} | Total: {total}")
        except:
    
            continue
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="do_action"]/div[1]/div/div/a').click()

    wait = WebDriverWait(driver, 10)
    address = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="cart_items"]/div/div[2]/h2')))
    print(address.text)

    wait = WebDriverWait(driver, 10)
    delevery_address = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address_delivery"]')))
    print(delevery_address.text)

    wait = WebDriverWait(driver, 10)
    billing_address = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="address_invoice"]')))
    print(billing_address.text)

    time.sleep(5)

    message = driver.find_element(By.XPATH, '//*[@id="ordermsg"]/textarea')
    driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", message)
    print(message.text)
    time.sleep(3)

    message_text = "Thank you ! mohon bantuannya"
    message_field = driver.find_element(By.XPATH, '//*[@id="ordermsg"]/textarea')
    message_field.send_keys(message_text)
    time.sleep(5)

    driver.find_element(By.XPATH, '//*[@id="cart_items"]/div/div[7]/a').click()