# Amazon-Automation-Login
This project automates the process of logging into Amazon using Selenium and extracting OTP from emails using IMAP. It performs specific actions on Amazon Music once logged in.

**Features**

    Automated Login: Automates the login process for Amazon using Selenium WebDriver.
    OTP Extraction: Extracts OTP from Gmail using IMAP and verifies it for logging in.
    Profile Management: Manages multiple user profiles for separate sessions.
    Error Handling: Comprehensive error handling for various stages of the login process.
    Reusable Components: Modular functions for email handling, password input, OTP input, and button interactions.

**Prerequisites**

    Python 3.x
    Google Chrome
    ChromeDriver
    Selenium
    IMAPLib
    email
    time
    re
    os

**Usage**

Prepare Email Credentials File

    Create a file named accounts.txt in the format:
    email1:password1:app-specific-password1
    email2:password2:app-specific-password2

Run the Script

    python amazon_login.py

**Code Overview**

Functions

    get_otp(useremail, userpassword): Fetches OTP from Gmail.
    profile(index): Manages user profile directories.
    email_func(driver, email_data): Inputs email into Amazon login form.
    pass_func(driver, password_data): Inputs password into Amazon login form.
    signin_button(driver): Clicks on the sign-in button.
    read_credentials(file_path): Reads credentials from a file.
    otp_func(driver, otp): Inputs OTP into Amazon verification form.

Main Execution

    Reads credentials from accounts.txt.
    Iterates over each set of credentials.
    Manages user profiles.
    Performs login actions including email and password input, OTP extraction, and verification.

Contributing

    Fork the repository.
    Create your feature branch (git checkout -b feature/your-feature).
    Commit your changes (git commit -m 'Add your feature').
    Push to the branch (git push origin feature/your-feature).
    Open a pull request.
Acknowledgements

    Selenium
    IMAPLib
    Python Community

Feel free to contribute, raise issues, or suggest features!
