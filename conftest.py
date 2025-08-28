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
            user_agent="MyCustomUserAgent/1.0",
            record_video_dir="./test-results/videos"  # Directory to save videos
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