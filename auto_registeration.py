from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import undetected_chromedriver as uc
import time

# from getActivateLink import get_activation_link

# URL you want to open
RegisterURL = "https://visa.vfsglobal.com/ago/en/prt/register"
LoginURL = "https://visa.vfsglobal.com/ago/en/prt/login"

### Register User
email = "you@gmail.com"
password = "your password"
nation_number = "your nation number"
phone_suffix = "your phone number"

driver = uc.Chrome()



try:
    # Process register
    driver.get(RegisterURL)
    driver.maximize_window()
    # Accept cookies
    cookie_passing = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
    )
    cookie_passing.click()

    # Wait for the email field to be present
    email_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'inputEmail'))
    )
    email_field.clear()  # Clear the field if needed
    email_field.send_keys(email)
    print("Print email")

    # Wait for the password field to be present and enter password
    password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'password'))
    )
    password_field.clear()  # Clear the field if needed
    password_field.send_keys(password)
    print("Print password")

    # Wait for the confirm_password field to be present and enter confirm_password
    confirm_password_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'confirmPassword'))
    )
    confirm_password_field.clear()  # Clear the field if needed
    confirm_password_field.send_keys(password)
    print("Print confirm password")

    time.sleep(15)

    # # Select mobile nation number
    nation_number_field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, "//div[contains(@class, 'mat-mdc-form-field-infix') and contains(@class, 'ng-tns-c75-3')]"))
    )
    nation_number_field.click()

    # Find specific country
    parent_tag = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//*[contains(@class, 'ng-trigger') and contains(@class, 'ng-trigger-transformPanel')]"))
    )
    baby_tags = parent_tag.find_elements(By.TAG_NAME, 'span')

    for tag in baby_tags:

        if nation_number in tag.text:
            print(tag.text)
            tag.click()
            break
    print("Select nation")
    time.sleep(1)
    
    
    # Wait for the phone suffix field to be present and enter phone suffix field
    phone_suffix_field = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'mat-input-3'))
    )
    phone_suffix_field.clear()  # Clear the field if needed
    phone_suffix_field.send_keys(phone_suffix)
    
    print("click nation number")

    for i in range(1, 4):
        checkbox = driver.find_element(By.ID, f'mat-mdc-checkbox-{i}-input')
        driver.execute_script("arguments[0].click();", checkbox)
        time.sleep(1)


    # Assuming there's a button to submit the registration form
    submit_button = driver.find_element(By.XPATH, '//button[@type="submit"]')
    driver.execute_script("arguments[0].click();", submit_button)
    time.sleep(1)
    print("Submit")

    time.sleep(10)
    # activation_link = get_activation_link(email=email, password=password)
    # time.sleep(1)
    # driver.get(activation_link)
    # time.sleep(1)
    
except Exception as e:
    print(f"An error occurred: {e}")
finally:
    # Close the browser
    driver.quit()






