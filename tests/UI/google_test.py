from playwright.sync_api import Page, expect
from pages.page_google import googlePage

def test_google_search(page: Page):
        google_page = googlePage(page)
        google_page.navigate()
        # google_page.screenshot(path="./screenshots/googletest.png")
        google_page.search("Playwright Python")
        expect (google_page.googleContent()).to_be_visible()

# venv/Scripts/activate
# pytest ./tests/UI/google_test.py --headed --browser=chromium --tracing=on