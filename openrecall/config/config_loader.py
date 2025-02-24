import json
import os

CONFIG_FILE = "openrecall/config/config.json"

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return {}
    with open(CONFIG_FILE, "r") as file:
        return json.load(file)


def update_config(config,new_data):
    config.update(new_data)
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file, indent=4)


if __name__ == '__main__':
    config = load_config()
    update_config({"general": {"theme": "light"}})
