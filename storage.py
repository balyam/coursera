import argparse
import os
import json
import tempfile


parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', type=str)
parser.add_argument('-v', '--val', type=str)

args = parser.parse_args()
print(args.val)

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


with open(storage_path, 'r') as f:

    try:
        json_data = json.load(f)
        print("File opened")
    except Exception as e:
        json_data = {}
        print("File created")

if args.val:
    with open(storage_path, 'w') as fw:
        if args.key in json_data.keys():
            json_data[args.key].append(args.val)
        else:
            json_data[args.key] = [args.val]
        json.dump(json_data, fw)
else:
    with open(storage_path, 'r') as fr:
        k = json.load(fr)
        print(", ".join(k[args.key]))


