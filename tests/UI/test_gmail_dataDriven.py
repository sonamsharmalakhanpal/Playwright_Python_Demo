import re
from playwright.sync_api import Page
from pages.gmail_login_page import gmailPage
import pytest


# def test_gmail_login(page: Page):
#     gmail_page = gmailPage(page)
#     # Navigate to Gmail login page
#     gmail_page.navigate()
#     # Perform login
#     gmail_page.login("muneet.gill1908@gmail.com", "Visa@123456")
    

    
def get_csv_data()-> list:
        import csv
        data = []
        with open('./test-data/credential.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header row
            for row in reader:
                data.append(row)
        return data
    
@pytest.mark.parametrize("username,password", get_csv_data())
def test_gmail_login_dataDriven(page: Page, username, password):
    gmail_page = gmailPage(page)
    # Navigate to Gmail login page
    gmail_page.navigate()
    # Perform login
    # gmail_page.login("muneet.gill1908@gmail.com", "Visa@123456")
    gmail_page.login(username, password) 
        
    

# venv/Scripts/activate
# pytest ./tests/UI/test_gmail_dataDriven.py --headed --browser=chromium --tracing=on
# playwright show-trace ./test-results/trace.zip