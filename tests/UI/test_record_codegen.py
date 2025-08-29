import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.locator("input[name=\"q\"]").click()
    page.locator("input[name=\"q\"]").fill("Sonam Lakhanpal")
    page.locator("input[name=\"q\"]").press("Enter")
    page.locator("text=Sonam Lakhanpal - YouTube").click()
    expect(page).to_have_url(re.compile(".*youtube.*")) 
    expect(page.locator("text=Sonam Lakhanpal - YouTube")).to_be_visible()
    
    # pytest ./tests/UI/test_record_codegen.py