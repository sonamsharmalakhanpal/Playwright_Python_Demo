from playwright.sync_api import Page, expect

class bingPage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("//textarea[@id='sb_form_q']")
        self.bingLogo = page.locator("//*[@title='Back to Bing search']")

    def navigate(self):
        self.page.goto("https://www.bing.com/")
        
    def bingsearch(self, query):
        self.search_box.type(query)
        self.search_box.press("Enter")

    def bingContent(self):
        expect(self.bingLogo).to_be_visible()