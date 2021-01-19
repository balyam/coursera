import argparse
import os
import json
import tempfile


parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', type=str)
parser.add_argument('-v', '--val', type=str)

args = parser.parse_args()
# print(args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
# storage_path = '777.txt'

try:
    with open(storage_path, 'r') as f:
        try:
            json_data = json.load(f)
        except Exception as e:
            json_data = {}
except Exception as e:
    with open(storage_path, 'w') as fn:
        json_data = {}

if args.val:
    with open(storage_path, 'w') as fw:
        if args.key in json_data.keys():
            json_data[args.key].append(args.val)
        else:
            json_data[args.key] = [args.val]
        json.dump(json_data, fw)
else:
    with open(storage_path, 'r') as fr:
        if fr.read():
            fr.seek(0)
            k = json.load(fr)
            if args.key in k.keys():
                print(", ".join(k[args.key]))
            else:
                print("")
        else:
            print(" ")
