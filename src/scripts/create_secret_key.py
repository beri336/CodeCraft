# src/scripts/create_secret_key.py

import secrets
import json
from pathlib import Path
from typing import Optional


def create_secret_key(config_path: str = "config.json") -> Optional[str]:
    """
    Generate a new secret key and save it to a config.json file.

    Args:
        config_path (str): Path to the config file. Defaults to "config.json".

    Returns:
        str: The generated SECRET_KEY, or None if file already exists.

    Raises:
        IOError: If the config file cannot be written.
        json.JSONDecodeError: If existing config is invalid JSON.

    Notes:
        - If config.json does not exist, it will be created with the generated SECRET_KEY.
        - If config.json already exists, no changes will be made.
    """
    config_file = Path(config_path)
    
    if not config_file.parent.exists():
        raise IOError(f"Directory does not exist: {config_file.parent}")
    
    if config_file.exists():
        print(f"ℹ️  {config_path} already exists. No changes made.")
        return None
    
    try:
        # generate safe secret key (32 bytes = 64 hex characters)
        key = secrets.token_hex(32)
        
        config = {
            "SECRET_KEY": key
        }
        
        with open(config_file, "w") as config_file_handle:
            json.dump(config, config_file_handle, indent=4)
        
        print(f"✅ {config_path} created successfully")
        print(f"   SECRET_KEY: {key}")
        
        return key
        
    except IOError as e:
        print(f"❌ Error writing config file: {e}")
        raise
    except json.JSONDecodeError as e:
        print(f"❌ JSON encoding error: {e}")
        raise
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        raise


if __name__ == "__main__":
    create_secret_key()
