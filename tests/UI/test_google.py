from playwright.sync_api import sync_playwright

def test_api_response():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto("https://google.com")
        page.screenshot(path="googletest.png")
        browser.close()

    # venv/Scripts/activate
    # pytest ./tests/UI/test_google.py --browser=chromium --headed --video=on