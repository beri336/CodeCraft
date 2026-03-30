# src/services/code_service.py

"""Handle code input and language selection."""

from pygments.lexers import get_all_lexers
from typing import Tuple, List, Dict, Any


def get_all_available_lexers() -> List[Tuple[str, Tuple[str, ...]]]:
    """
    Get all available Pygments lexers.
    
    Returns:
        List of tuples containing (lexer_name, aliases).
    """
    return [(lexer[0], lexer[1]) for lexer in get_all_lexers()]


def prepare_code_context(code: str, language: str) -> Dict[str, Any]:
    """
    Prepare context dictionary for code input template.
    
    Args:
        code (str): The code string.
        language (str): The programming language.
        
    Returns:
        dict: Context for template rendering.
    """
    lines = code.split("\n")
    max_chars = len(max(lines, key=len)) if lines else 0
    
    return {
        "message": "Paste your Code",
        "code": code,
        "num_lines": len(lines),
        "max_chars": max_chars,
        "language": language,
        "lexers": get_all_available_lexers()
    }


def validate_code_input(code: str) -> str:
    """
    Validate and clean code input.
    
    Args:
        code (str): Raw code input from form.
        
    Returns:
        str: Validated code or fallback value.
    """
    if not code or not code.strip():
        from config import NO_CODE_FALLBACK
        return NO_CODE_FALLBACK
    return code
