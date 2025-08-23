from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://google.com")
    page.screenshot(path="example.png")
    browser.close()

    # pytest ./tests/UI/test_google.py --browser=chromium --headed