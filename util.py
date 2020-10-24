# -*- coding:utf-8 -*-
import json
import sys
sys.path.append(".")
def get_config():
    with open('./config.json', 'r') as f:
        str_config = f.read()
    config = json.loads(str_config)
    return config

if __name__ == '__main__':
    print(get_config())
