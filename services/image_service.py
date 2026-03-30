# src/services/image_service.py

"""Handle screenshot generation."""

from flask import Request
import base64
from typing import Optional
from src.utils import take_screenshot_from_url


def prepare_session_data(request: Request, style_url: str) -> dict:
    """
    Prepare session data for screenshot capture.
    
    Args:
        request: Flask request object.
        style_url: URL to the style page.
        
    Returns:
        dict: Session data for Playwright.
        
    Raises:
        ValueError: If session cookie not found.
    """
    session_cookie_name = "session"
    session_cookie_value = request.cookies.get(session_cookie_name)
    
    if not session_cookie_value:
        raise ValueError("No session cookie found")
    
    return {
        "name": session_cookie_name,
        "value": session_cookie_value,
        "url": request.host_url.rstrip("/"),
    }


def generate_code_screenshot(request: Request, style_url: str) -> Optional[str]:
    """
    Generate a screenshot of the code and return as base64.
    
    Args:
        request: Flask request object.
        style_url: Full URL to the style page.
        
    Returns:
        str: Base64 encoded image or None if failed.
        
    Raises:
        ValueError: If session data is invalid.
        Exception: If screenshot generation fails.
    """
    try:
        session_data = prepare_session_data(request, style_url)
        image_bytes = take_screenshot_from_url(style_url, session_data)
        
        if image_bytes is None:
            return None
        
        return base64.b64encode(image_bytes).decode("utf-8")
        
    except Exception as e:
        print(f"❌ Screenshot generation failed: {e}")
        raise


def prepare_image_context(image_b64: str) -> dict:
    """Prepare context for image display template."""
    return {
        "message": "DONE!",
        "image_b64": image_b64,
    }
