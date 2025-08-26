from playwright.sync_api import sync_playwright
from pages.page_google import googlePage
import pytest

@pytest.mark.usefixtures("page")
class TestGoogle:
    def test_google_search(self, page):
        google_page = googlePage(page)
        google_page.navigate()
        # google_page.screenshot(path="./screenshots/googletest.png")
        google_page.search()
        
        # google.search("Playwright Python")
