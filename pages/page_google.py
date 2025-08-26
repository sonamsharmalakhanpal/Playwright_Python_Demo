class googlePage:
    def __init__(self, page):
        self.page = page
        self.search_box = page.locator("input[name='q']")
        self.search_button = page.locator("input[name='btnK']")

    async def navigate(self):
        await self.page.goto("https://www.google.com")
        wait_for_load_state="networkidle"
        await self.page.wait_for_load_state(wait_for_load_state)
        
        
    async def search(self):
        await self.search_box.fill("playwright python")
        await self.search_button.click()