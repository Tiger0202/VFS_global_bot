from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyautogui
import undetected_chromedriver as uc
import imaplib
import email
import re

def get_otp_from_email(email_user, email_pass):
    mail = imaplib.IMAP4_SSL('imap.gmail.com')
    mail.login(email_user, email_pass)
    mail.select('inbox')
    result, data = mail.search(None, 'UNSEEN')
    mail_ids = data[0]
    id_list = mail_ids.split()
    for e_id in id_list:
        result, data = mail.fetch(e_id, '(RFC822)')
        msg = email.message_from_bytes(data[0][1])
        payload = msg.get_payload(decode=True)
        if payload:
            body = payload.decode()
            otp_match = re.search(r'\b\d{6}\b', body)
            if otp_match:
                otp = otp_match.group(0)
                break
    mail.logout()
    return otp

USERNAME = "shinyawatanabe817@gmail.com"
PASSWORD = "Pwd123!@#"
EMAILPASS = "kutc udxv zqpa bdno"

driver = uc.Chrome()

try:
    driver.get('https://visa.vfsglobal.com/ago/en/prt/login')
    time.sleep(20)
    cookie_passing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_passing.click()
    try:
        username_field = driver.find_element(By.ID, 'email')
    except:
        print('username field not found')
    username_field.send_keys(USERNAME)
    password_field = driver.find_element(By.ID, 'mat-input-4')
    password_field.send_keys(PASSWORD)
    time.sleep(3)
    for i in PASSWORD:
        if i.islower():
            driver.find_element(By.XPATH, f'//button[@name="{i}"]').click()
            time.sleep(1)
        else: 
            if i.isupper():
                driver.find_element(By.XPATH, '//button[@name="{shift}"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, f'//button[@name="{i}"]').click()
                time.sleep(1)
                driver.find_element(By.XPATH, '//button[@name="{shift}"]').click()
                time.sleep(1)
            else: 
                if i.isdigit():
                    driver.find_element(By.XPATH, '//button[@name="{numeric}"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, f'//button[@name="{i}"]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//button[@name="{alphabetic}"]').click()
                    time.sleep(1)
                else:    
                    password_char = driver.find_element(By.XPATH, '//button[@name="{numeric}"]').click()
                    time.sleep(1)
                    if i in ['/', ';', ')', '@', '$', '"', ':', '&', '(', '-']:
                        driver.find_element(By.XPATH, f'//button[@name="{i}"]').click()
                        time.sleep(1)
                        driver.find_element(By.XPATH, '//button[@name="{alphabetic}"]').click()
                        time.sleep(1)
                    else:
                        driver.find_element(By.XPATH, '//button[@name="{symbolic}"]').click()
                        time.sleep(1)
                        driver.find_element(By.XPATH, f'//button[@name="{i}"]').click()
                        time.sleep(1)
                        driver.find_element(By.XPATH, '//button[@name="{alphabetic}"]').click()
                        time.sleep(1)
    driver.find_element(By.XPATH, "//h1[text()='Sign in']").click()
    time.sleep(10)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(5)
    button = driver.find_element(By.XPATH, "//button[span[text()=' Sign In ']]")
    window_position = driver.get_window_position()
    print(f"Element position: x={window_position['x']}, y={window_position['y']}")
    x, y = window_position['x'] + button.location['x'] + 25, window_position['y'] + button.location['y'] + 30
    pyautogui.click(x=x, y=y)
    time.sleep(5)
    button.click()
    time.sleep(40)
    otp_code = get_otp_from_email(USERNAME, EMAILPASS)
    print(otp_code)
    otp_field = driver.find_element(By.ID, 'mat-input-5')
    otp_field.send_keys(otp_code)
    for i in otp_code:
        driver.find_element(By.XPATH, f'//button[@name="{i}"]').click()
        time.sleep(1)
    driver.find_element(By.XPATH, "//h1[text()='Sign in']").click()
    time.sleep(5)
    otp_button = driver.find_element(By.XPATH, "//button[span[text()=' Sign In ']]")
    x, y = window_position['x'] + otp_button.location['x'] + 25, window_position['y'] + otp_button.location['y'] + 30
    pyautogui.click(x=x, y=y)
    otp_button.click()
    time.sleep(50)
finally:
    driver.quit()

