# learning about great instruments: JSON, argparse
# learning argparse pulls me to make in windows prompt 
# my control panel for arduino 
# interesting use of temp files, take on mind 

import os
import tempfile
import json
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--key", help="get value if only, puts key & val if with --val")
parser.add_argument("--val", help="puts key & val")
args = parser.parse_args()

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')
if not os.path.exists(storage_path):
    with open(storage_path, 'w') as f:
        f.write(json.dumps({}))

if(args.key and args.val): 
    with open(storage_path, 'r') as f:
        
        json_temp = f.read()
        dict_temp = json.loads(json_temp)
        if args.key in dict_temp:
            dict_temp[args.key].append(args.val)
        else:
            dict_temp[args.key] = [args.val]
        json_temp = json.dumps(dict_temp)

    with open(storage_path, 'w') as f:

        f.write(json_temp)

elif(args.key):
    with open(storage_path, 'r') as f:
        
        json_temp = f.read()
        dict_temp = json.loads(json_temp)
        answer = dict_temp.get(args.key, None)
        if answer:
            print(', '.join(answer))
        else:
            print(answer)