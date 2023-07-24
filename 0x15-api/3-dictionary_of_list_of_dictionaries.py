#!/usr/bin/python3
"""Extend Task#0 to export data in JSON format."""

import json
import requests
import sys


if __name__ == '__main__':
    users = requests.get("https://jsonplaceholder.typicode.com/users/").json()
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    etasks = {}
    for user in users:
        eid = user.get("id")
        etasks['{}'.format(eid)] = []
        for task in tasks:
            userId = task.get('userId')
            if userId == int(eid):
                info = {}
                info["username"] = user.get('username')
                info["completed"] = task.get('completed')
                info["task"] = task.get('title')
                etasks[str(eid)].append(info)

    with open('todo_all_employees.json'.format(eid), 'w') as json_file:
        jsn = json.dumps(etasks, sort_keys=True)
        json_file.write(jsn)
