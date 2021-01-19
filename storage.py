import argparse
import os
import json
import tempfile


parser = argparse.ArgumentParser()

parser.add_argument('-k', '--key', type=str)
parser.add_argument('-v', '--val', type=str)

args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


with open('777.txt', 'w') as f:

    try:
        json_data = json.loads(f)
        print("File opened")
    except Exception as e:
        json_data = {}
        print("File created")

    if args.val:
        if args.key in json_data.keys():
            json_data[args.key].append(args.val)
        else:
            json_data[args.key] = args.val
        json.dump(json_data, f)
    else:
        k = json.loads(f)
        print(k[args.key])

