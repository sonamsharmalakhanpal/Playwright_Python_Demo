import re
from playwright.sync_api import Page
from pages.gmail_login_page import gmailPage

def test_gmail_login(page: Page):
    gmail_page = gmailPage(page)
    # Navigate to Gmail login page
    gmail_page.navigate()
    # Perform login
    gmail_page.login("muneet.gill1908@gmail.com", "Visa@123456")

# venv/Scripts/activate
# pytest ./tests/UI/test_gmail.py --headed --browser=chromium --tracing=on
