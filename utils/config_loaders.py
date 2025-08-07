import yaml 
import os 

def load_config (file_path: str = f"{os.getcwd()}\\config\\config.yml") -> dict:
    with open(file_path, "r") as f:
        config = yaml.safe_load(f)
        
    return config