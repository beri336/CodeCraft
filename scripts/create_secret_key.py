# create_secret_key.py

import secrets
import json
import os

def create_secret_key():
    """
    Generate a new secret key and save it to a config.json file.

    - If config.json does not exist, it will be created with the generated SECRET_KEY.
    - If config.json already exists, no changes will be made.

    Outputs:
        A message indicating whether the file was created or already exists.
    """
    # generate a new secret key as a hex string
    key = secrets.token_hex()
    
    # define the configuration structure
    config = {
        "SECRET_KEY": key
    }
    
    # check if config.json already exists
    if not os.path.exists("config.json"):
        # create and write the secret key to config.json
        with open("config.json", "w") as config_file:
            json.dump(config, config_file, indent=4)
        print(f"config.json created with SECRET_KEY:\n\t-> {key}")
    else:
        # notify the user if config.json already exists
        print("config.json already exists. No changes made.")

if __name__ == "__main__":
    # run the create_secret_key function when executed as a script
    create_secret_key()