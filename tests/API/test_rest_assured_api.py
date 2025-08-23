import pytest
from playwright.sync_api import sync_playwright

def test_api_response():
    with sync_playwright() as p:
        request = p.request.new_context()
        response = request.get("https://jsonplaceholder.typicode.com/posts/1")
        json_status = response.status
        json_data = response.json()
        print("Response JSON:", json_data)
        assert response.status == 200
        assert json_data["id"] == 1
        
        request.dispose()
        print("API test completed successfully.")

#  pytest tests/API/test_rest_assured_api.py