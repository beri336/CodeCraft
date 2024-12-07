# utils.py

from playwright.sync_api import sync_playwright

def take_screenshot_from_url(url, session_data):
    with sync_playwright() as playwright:
        webkit = playwright.webkit
        browser = webkit.launch()  # Launch headless browser
        browser_context = browser.new_context(device_scale_factor=2)  # Picture is not pixelated
        browser_context.add_cookies([{
            'name': session_data['name'],
            'value': session_data['value'],
            'url': session_data['url']
        }])
        page = browser_context.new_page()
        page.goto(url)
        screenshot_bytes = page.locator(".code").screenshot()
        browser.close()
        return screenshot_bytes