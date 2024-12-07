# utils.py

from playwright.sync_api import sync_playwright

def take_screenshot_from_url(url, session_data):
    """
    Capture a screenshot of a specific element on a webpage using Playwright.

    Args:
        url (str): The URL of the webpage to capture.
        session_data (dict): Session information for the browser, including:
            - 'name' (str): The name of the session cookie.
            - 'value' (str): The value of the session cookie.
            - 'url' (str): The base URL for the cookie.

    Returns:
        bytes: The screenshot of the element with class 'code' as a byte array.
    """
    with sync_playwright() as playwright:
        # use the WebKit browser engine
        webkit = playwright.webkit
        browser = webkit.launch() # launch a headless browser
        
        # create a browser context with a high device scale factor for better quality
        browser_context = browser.new_context(device_scale_factor=2)

        # add session cookies to the browser context
        browser_context.add_cookies([{
            'name': session_data['name'],
            'value': session_data['value'],
            'url': session_data['url']
        }])

        # open a new page and navigate to the target URL
        page = browser_context.new_page()
        page.goto(url)

        # capture a screenshot of the element with class 'code'
        screenshot_bytes = page.locator(".code").screenshot()

        # close the browser
        browser.close()

        # return the screenshot as a byte array
        return screenshot_bytes