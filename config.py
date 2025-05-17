import yaml
from pathlib import Path
from typing import Dict, Any

def load_config(config_path: str = "config.yaml") -> Dict[str, Any]:
    """Load configuration from YAML file"""
    with open(config_path, 'r') as f:
        config = yaml.safe_load(f)
    return config


config = load_config()

# module-level variables
APP_NAME = config['app']['name']
APP_VERSION = config['app']['version']
DEBUG = config['app']['debug']
DATABASE_URL = config['database']['url']
SERVER_HOST = config['server']['host']
SERVER_PORT = config['server']['port']