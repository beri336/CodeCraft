# src/utils.py

from playwright.sync_api import sync_playwright
from typing import Optional


def take_screenshot_from_url(url: str, session_data: dict) -> Optional[bytes]:
    """
    Capture a screenshot of a specific element on a webpage using Playwright.

    Args:
        url (str): The URL of the webpage to capture.
        session_data (dict): Session information for the browser, including:
            - 'name' (str): The name of the session cookie.
            - 'value' (str): The value of the session cookie.
            - 'url' (str): The base URL for the cookie.

    Returns:
        bytes: The screenshot of the element with class 'code' as a byte array,
               or None if the capture fails.
        
    Raises:
        TimeoutError: If page load or element wait times out.
        ValueError: If session_data is missing required keys.
    """
    # validate input data
    required_keys = {'name', 'value', 'url'}
    if not isinstance(session_data, dict) or not required_keys.issubset(session_data.keys()):
        raise ValueError(f"session_data must contain keys: {required_keys}")
    
    try:
        with sync_playwright() as playwright:
            browser = playwright.webkit.launch(headless=True)
            
            try:
                browser_context = browser.new_context(device_scale_factor=2)
                
                try:
                    # add session cookie
                    browser_context.add_cookies([{
                        'name': session_data['name'],
                        'value': session_data['value'],
                        'url': session_data['url']
                    }])

                    page = browser_context.new_page()
                    
                    try:
                        page.goto(url, wait_until="networkidle", timeout=30000)

                        page.locator(".code").wait_for(state="visible", timeout=10000)

                        screenshot_bytes = page.locator(".code").screenshot()
                        
                        return screenshot_bytes
                        
                    except Exception as e:
                        print(f"Fehler beim Screenshot: {e}")
                        raise
                    finally:
                        page.close()
                        
                finally:
                    browser_context.close()
                    
            finally:
                browser.close()
                
    except TimeoutError as e:
        print(f"Timeout Error: {e}")
        raise
    except Exception as e:
        print(f"Unerwarteter Fehler: {e}")
        raise
