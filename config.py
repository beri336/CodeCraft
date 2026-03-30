# config.py

"""Application configuration and constants."""

import json
from pathlib import Path
from typing import Optional


# default values
PLACEHOLDER_CODE = "print('HELLO, WORLD!')"
DEFAULT_STYLE = "monokai"
DEFAULT_LANGUAGE = "python"
NO_CODE_FALLBACK = "#No Code Entered"

# app Configuration
DEBUG = True
HOST = "0.0.0.0"
PORT = 8080


def load_secret_key() -> bytes:
    """
    Load the secret key from config.json file.
    
    Returns:
        bytes: The secret key for Flask session management.
        
    Raises:
        FileNotFoundError: If config.json doesn't exist.
        json.JSONDecodeError: If config.json is invalid.
    """
    config_path = Path("config.json")
    
    if not config_path.exists():
        raise FileNotFoundError("config.json not found. Run: python create_secret_key.py")
    
    try:
        with open(config_path) as f:
            config = json.load(f)
        return config["SECRET_KEY"].encode()
    except KeyError:
        raise KeyError("SECRET_KEY not found in config.json")
    except json.JSONDecodeError as e:
        raise json.JSONDecodeError(f"Invalid config.json: {e}", e.doc, e.pos)
