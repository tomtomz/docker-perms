
import os
import shutil
from pathlib import Path
import yaml
from collections import defaultdict

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)
    print(cfg)
    cfg = defaultdict(lambda: -1, cfg)
    for section in cfg:
        print(section)
        path = cfg[section].get('path')   
        perms = cfg[section].get('permissions')
        owner = cfg[section].get('owner')
        group = cfg[section].get('group')

with open('testing.csv','r') as f:
    lines = f.read().splitlines()
    for line in lines:
        items = line.split(",")
        if len(items) < 2:
            print(line + " path and permissions are required... Moving to next item")
            continue
        dirname = Path(items[0])
        perms = int(items[1],8)
        if dirname.is_dir():
            print("Changing path: " + items[0] + " permissions to " + items[1])
            os.chmod(dirname,perms)

            if len(items) > 2:
                owner = items[2].strip()
                if len(owner):
                    print("     changing owner to " + owner)
                    shutil.chown(dirname, user=owner)

            if len(items) > 3:
                group = items[3].strip()
                if (len(group)):
                    print( "     changing group to " + group)
                    shutil.chown(dirname, group=group)
        else:
            print(dirname, ' Does not exist')
