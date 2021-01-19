import argparse
import os
import json
import tempfile


parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', type=str)
parser.add_argument('-v', '--val', type=str)

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


with open('777.txt', 'r') as f:

    try:
        json_data = json.load(f)
        print("File opened")
    except Exception as e:
        json_data = {}
        print("File created")

if args.val:
    with open('777.txt', 'w') as fw:
        if args.key in json_data.keys():
            json_data[args.key].append(args.val)
        else:
            json_data[args.key] = [args.val]
        json.dump(json_data, fw)
else:
    with open('777.txt', 'r') as fr:
        k = json.load(fr)

        print(k[args.key])

