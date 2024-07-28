import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import imaplib
import email
from email.policy import default
import re


def get_otp(useremail, userpassword):
    user = useremail
    password = userpassword  # App-specific password
    imap_url = 'imap.gmail.com'

    def get_body(msg):
        """Function to extract email body."""
        if msg.is_multipart():
            for part in msg.iter_parts():
                if part.get_content_type() == "text/plain":
                    return part.get_payload(decode=True).decode()
                elif part.get_content_type() == "text/html":
                    return part.get_payload(decode=True).decode()
        else:
            return msg.get_payload(decode=True).decode()

    def fetch_latest_email(con, sender_email):
        """Function to fetch the latest email from a specific sender."""
        result, data = con.search(None, f'(FROM "{sender_email}")')
        if result != 'OK':
            print("Error searching emails:", result)
            return None
        
        email_ids = data[0].split()
        if not email_ids:
            return None

        latest_email_id = email_ids[-1]
        typ, msg_data = con.fetch(latest_email_id, '(RFC822)')
        if typ != 'OK':
            print("Error fetching email:", typ)
            return None
        
        return msg_data

    def extract_otp(email_body):
        """Function to extract OTP from email body."""
        # Regex pattern to match the OTP within the specified <td> style
        otp_pattern = re.compile(r'<td[^>]?background-color:\s#D3D3D3[^>]?>\s<p>\s*(\d{6})\s*</p>\s*</td>', re.IGNORECASE)
        match = otp_pattern.search(email_body)
        if match:
            return match.group(1).strip()
        return None

    con = imaplib.IMAP4_SSL(imap_url)
    con.login(user, password)
    con.select('INBOX')

    # Fetch the latest email from 'account-update@amazon.com'
    sender_email = 'account-update@amazon.com'
    latest_email_data = fetch_latest_email(con, sender_email)

    if latest_email_data:
        for response_part in latest_email_data:
            if isinstance(response_part, tuple):
                msg = email.message_from_bytes(response_part[1], policy=default)
                sender = msg['From']
                email_body = get_body(msg)
                # Extract OTP
                otp = extract_otp(email_body)
                if otp:
                    print(f"Sender: {sender}")
                    print(f"OTP: {otp}")
                    return otp
                else:
                    print(f"Sender: {sender}")
                    print("OTP not found.")
                    return None
    else:
        print("No emails found from", sender_email)
        return None

def profile(index):
    profile_directory_name = f"profilechrome-{index}"
    full_path = os.path.join(os.getcwd(), profile_directory_name)
    if not os.path.exists(full_path):
        os.makedirs(full_path)
        print(f"The directory '{full_path}' was created.")
    return full_path

def email_func(driver, email_data):
    try:
        email_input = driver.find_element(By.ID, "ap_email")
        email_input.send_keys(email_data)
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        time.sleep(10)
    except Exception as e:
        print(f"Error in email_func: {e}")

def pass_func(driver, password_data):
    try:
        password_input = driver.find_element(By.ID, "ap_password")
        password_input.send_keys(password_data)
        time.sleep(2)
        # Click on the Remember Me checkbox
        try:
            remember_me_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="rememberMe"][type="checkbox"][tabindex="5"]')
            remember_me_checkbox.click()
        except:
            try:
                remember_me_checkbox = driver.find_element(By.CSS_SELECTOR, 'input[name="rememberMe"][type="checkbox"][tabindex="4"]')
                remember_me_checkbox.click()
            except:
                pass
        time.sleep(1)
        sign_in_submit = driver.find_element(By.ID, "signInSubmit")
        sign_in_submit.click()
    except Exception as e:
        print(f"Error in pass_func: {e}")

def signin_button(driver):
    try:
        time.sleep(10)
        sign_in_button = driver.find_element(By.ID, "signInButton")
        sign_in_button.click()
        time.sleep(10)
    except Exception as e:
        print(f"Error in signin_button: {e}")

def read_credentials(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    credentials = [tuple(line.strip().split(':')) for line in lines]
    return credentials

def otp_func(driver, otp):
    try:
        otp_input = driver.find_element(By.ID, "input-box-otp")
        otp_input.send_keys(otp)
        time.sleep(5)  # Replace with WebDriverWait for better practice
        # Attempt to find and click the submit button by class name
        try:
            submit_button = driver.find_element(By.CSS_SELECTOR, ".a-button-input")
            submit_button.click()
        except NoSuchElementException:
            # If the first method fails, try finding by ID
            submit_button = driver.find_element(By.ID, "cvf-submit-otp-button-announce")
            submit_button.click()
    except Exception as e:
        print(f"Error in otp_func: {e}")

file_path = "C:\\Users\\PC\\Downloads\\accounts.txt"
credentials = read_credentials(file_path)
print(credentials)

for index, (email_address, password, user_password) in enumerate(credentials, start=1):
    useremail = str(email_address)
    userpassword = user_password.replace(" ", "")  ### Remove spaces from user_password
    print('user password is , ', userpassword)
    
    # otp = get_otp(useremail, userpassword)  ### for testing purpose of OTP
    # print('OTP', otp)  ### for testing purpose of OTP
    
    full_path = profile(index)
    chrome_options = Options()
    chrome_options.add_argument(f"user-data-dir={full_path}")
    chrome_options.add_argument("--disable-gpu")
    webdriver_service = Service()
    driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
    url = "https://music.amazon.com/albums/B0BZGZCB5Q"
    driver.get(url)
    time.sleep(10)

    try:
        signin_button(driver)
        email_func(driver, email_address)
        pass_func(driver, password)
        time.sleep(10)
        current_url = driver.current_url
        if current_url == 'https://www.amazon.com/':
            driver.get(url)
            signin_button(driver)
        email_func(driver, email_address)
        pass_func(driver, password)
        # Check if OTP input box is present
        otp_input_box = driver.find_elements(By.ID, "input-box-otp")
        if otp_input_box:
            time.sleep(30)  # Increase the following sleep command if needed to enter the verification OTP from email
            otp = get_otp(useremail, userpassword)
            print('OTP', otp)
            time.sleep(30)
            otp_func(driver, otp)
        email_func(driver, email_address)
        pass_func(driver, password)
        print('The code has been run successfully. Remove this print and the following sleep')
        # time.sleep(30)  #### Extra command just for demo
    except Exception as e:
        print(f"Error: {e}")
    finally:
        driver.quit()
