# Amazon Music Login Automation

## Overview
This project automates the login process for Amazon Music, including OTP (One-Time Password) verification sent via email. It uses Python, Selenium for web automation, and IMAP for email handling.

## Features
- Automates the login process to Amazon Music.
- Handles OTP verification via email.
- Uses Selenium for web automation.
- Uses IMAP to fetch OTP from Gmail.

## Requirements
- Python 3.x
- Selenium
- imaplib
- email
- re
- chromedriver-autoinstaller

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/amazon-music-login-automation.git
    ```
2. Navigate to the project directory:
    ```sh
    cd amazon-music-login-automation
    ```
3. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Ensure you have Google Chrome installed.
2. Prepare a text file `accounts.txt` with your email credentials in the following format:
    ```
    email_address:password:user_password
    ```
3. Run the script:
    ```sh
    python amazon_login.py
    ```

## Code Structure
- `amazon_login.py`: The main script that runs the automation.
- `requirements.txt`: List of required packages.

## Configuration
- The script reads credentials from a file named `accounts.txt`. Ensure the file is in the format:
    ```
    email_address:password:user_password
    ```
- The script uses a profile directory for each login attempt to maintain session data.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.



## Acknowledgements
- This project uses the [Selenium](https://selenium.dev/) library for web automation.
- IMAP is used for email handling.


