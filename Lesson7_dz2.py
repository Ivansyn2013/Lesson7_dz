import json
import os

ROOT = os.path.dirname(__file__)

with open('config.json','r', encoding = 'utf-8') as f:
    conf = json.load(f)

for dir_path in conf:
    fulldir_path = os.path.join(ROOT, dir_path)
    os.makedirs(fulldir_path, exist_ok = True)
    for file_name in conf[dir_path]:
        with open(os.path.join(fulldir_path, file_name), 'x', encoding='utf-8'):
            pass
