#!/usr/bin/env python

import sys
import json
import dateutil.parser as dp
from datetime import datetime

def extract_vars_from_payload(payload):
    try:
        bucket = payload['source']['bucket']
        endpoint = payload['source']['endpoint']
        path = payload['source']['path']
        version_ref = payload['version']['ref']
    except (KeyError, TypeError) as e:
        print("Error processing payload from concourse")
        print("Required source parameters are bucket, endpoint, path and version_ref")
        print(e)
        sys.exit(1)
    return(bucket, endpoint, path, version_ref)

if __name__ == "__main__":
    try:
        payload = sys.stdin.read()
        bucket, endpoint, path, version_ref = extract_vars_from_payload(json.loads(payload))
        metadata = [{"name": "bucket", "value": bucket}, {"name": "endpoint", "value": endpoint}, {"name": "path", "value": path}]

        if sys.argv[1] != "":
            file_info=json.loads(sys.argv[1])
            for file in file_info:
                new_time = dp.isoparse(file['last_changed'])
                file['last_changed'] = new_time.strftime("%d/%m/%Y, %H:%M:%S %Z")
                metadata.append({"name": f"{file['file_name']}", "value" : f"Size: {file['file_size']} bytes, Last-modified: {file['last_changed']}"})

        print(json.dumps({ "version": { "ref": version_ref }, "metadata": metadata }))

    except Exception as e:
        print("Unexpected error encountered in `main`")
        print(e)
        sys.exit(1)
