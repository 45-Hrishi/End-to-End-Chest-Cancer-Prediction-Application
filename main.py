import yaml
from pathlib import Path

with open("config/config.yaml") as yaml_file:
    content = yaml.safe_load(yaml_file)
    print(content)