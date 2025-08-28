from playwright.sync_api import Page, expect

class gmailPage:
    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.locator("input[type='email']")
        self.next_button = page.locator("button:has-text('Next')")
        self.password_input = page.locator("input[type='password']")
        self.inbox_label = page.locator("a[title^='Inbox']")

    def navigate(self):
        self.page.goto("https://gmail.com")

    def login(self, email: str, password: str):
        self.email_input.fill(email)
        self.next_button.click()
        self.page.wait_for_timeout(2000)  # Wait for password field to appear
        self.password_input.fill(password)
        self.next_button.click()
        # self.page.wait_for_load_state("networkidle")

    def verify_login(self):
        return self.inbox_label.is_visible()