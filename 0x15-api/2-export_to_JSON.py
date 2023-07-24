#!/usr/bin/python3
"""Extend Task#0 to export data in JSON format."""

import json
import requests
import sys


if __name__ == '__main__':
    eid = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(eid))
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    etasks = {}
    etasks['{}'.format(eid)] = []
    for task in tasks:
        userId = task.get('userId')
        if userId == int(eid):
            info = {}
            info["username"] = user.json().get('username')
            info["completed"] = task.get('completed')
            info["task"] = task.get('title')
            etasks[eid].append(info)

    with open('{}.json'.format(eid), 'w') as f:
        jsn = json.dumps(etasks)
        f.write(jsn)
