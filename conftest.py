import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
# def browser():
#     with sync_playwright() as p:
#         browser = p.chromium.launch(headless=False)
#         yield browser
#         browser.close()
def browser_context():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            viewport={"width": 1280, "height": 720},
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
            locale="en-US",
            timezone_id="America/New_York",
            geolocation={"longitude": -74.0060, "latitude": 40.7128},
            permissions=["geolocation"],
            device_scale_factor=1,
            is_mobile=False,
            accept_downloads=True,
            record_video_dir="./test-results/videos"
)
        # Start tracing
        context.tracing.start(screenshots=True, snapshots=True, sources=True)
        yield context
        # Stop tracing and export to trace.zip
        context.tracing.stop(path="./test-results/trace.zip")
        context.close()
        browser.close()
        
@pytest.fixture
def page(browser_context):
    page = browser_context.new_page()
    yield page
    page.close()