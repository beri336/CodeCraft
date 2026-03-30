# src/services/style_service.py

"""Handle syntax highlighting and style selection."""

from pygments import highlight
from pygments.formatters import HtmlFormatter
from pygments.lexers import get_lexer_by_name, get_all_lexers  # ← Ändere hier
from pygments.styles import get_all_styles  # ← Hier ist es!
from typing import Dict, Any, Tuple


def get_all_available_styles() -> list:
    """Get all available Pygments styles."""
    return list(get_all_styles())


def generate_highlighted_code(
    code: str,
    language: str,
    style: str
) -> Tuple[str, str, str]:
    """
    Generate HTML-formatted code with syntax highlighting.
    
    Args:
        code (str): Code to highlight.
        language (str): Programming language.
        style (str): Pygments style name.
        
    Returns:
        Tuple containing:
        - highlighted_html (str): HTML with highlighted code
        - style_defs (str): CSS style definitions
        - bg_color (str): Background color of the style
        
    Raises:
        ValueError: If language or style is invalid.
    """
    try:
        formatter = HtmlFormatter(style=style)
        lexer = get_lexer_by_name(language)
    except Exception as e:
        raise ValueError(f"Invalid language '{language}' or style '{style}': {e}")
    
    highlighted_code = highlight(code, lexer, formatter)
    style_defs = formatter.get_style_defs()
    bg_color = formatter.style.background_color
    
    return highlighted_code, style_defs, bg_color


def prepare_style_context(
    code: str,
    language: str,
    style: str
) -> Dict[str, Any]:
    """
    Prepare context dictionary for style selection template.
    
    Args:
        code (str): Code to highlight.
        language (str): Programming language.
        style (str): Selected Pygments style.
        
    Returns:
        dict: Context for template rendering.
    """
    highlighted_code, style_defs, bg_color = generate_highlighted_code(
        code, language, style
    )
    
    return {
        "message": "Select Your Style",
        "all_styles": get_all_available_styles(),
        "style": style,
        "style_definitions": style_defs,
        "style_bg_color": bg_color,
        "highlighted_code": highlighted_code,
    }
