import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.locator("input[name=\"q\"]").click()
    page.locator("input[name=\"q\"]").fill("Sonam Lakhanpal")
    page.locator("input[name=\"q\"]").press("Enter")
    
    # pytest ./tests/UI/test_record_codegen.py