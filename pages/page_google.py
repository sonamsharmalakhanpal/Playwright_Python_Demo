from playwright.sync_api import Page, expect

class googlePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("//textarea[@id='APjFqb']")
        self.googleHome = page.get_by_role("link", name="Go to Google Home")

    def navigate(self):
        self.page.goto("https://www.google.com/")
        try:
            self.page.get_by_role("button", name="Accept all").click()
        except:
            print("No popup to accept")
        
        
    def search(self, query):
        self.search_box.fill(query)
        self.search_box.press("Enter")

    def googleContent(self):
        expect(self.googleHome).to_be_visible()