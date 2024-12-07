# create_secret_key.py

import secrets
import json
import os

def create_secret_key():
    # generate a new secret key
    key = secrets.token_hex()
    
    # define the configuration structure
    config = {
        "SECRET_KEY": key
    }
    
    # Ccheck if config.json exists
    if not os.path.exists("config.json"):
        # write the configuration to config.json
        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)
        print(f"config.json created with SECRET_KEY:\n\t-> {key}")
    else:
        print("config.json already exists. No changes made.")


if __name__ == "__main__":
    create_secret_key()