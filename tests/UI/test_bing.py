from playwright.sync_api import sync_playwright
from playwright.sync_api import Page, expect
from pages.page_bing import bingPage
import pytest



def get_csv_data()-> list:
        import csv
        data = []
        with open('./test-data/googleSearchData.csv', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip the header row
            for row in reader:
                data.append(row[0])  # Assuming single column CSV, take the first element
        return data

@pytest.mark.parametrize("searchTerm", get_csv_data())
def test_bing_search(page: Page, searchTerm):
        bing_page = bingPage(page)
        bing_page.navigate()
        bing_page.bingsearch(searchTerm)
        # expect (bing_page.bingContent()).to_be_true()

    # venv/Scripts/activate
    # pytest ./tests/UI/test_bing.py --browser=chromium --headed --html=report.html 
   
    # playwright show-trace ./test-results/trace.zip
    # pip install pytest-html (install once before running above command for report generation)
    