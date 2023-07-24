#!/usr/bin/python3
"""Extend Task#0 to export data in the CSV format."""

if __name__ == "__main__":
    import csv
    import requests
    import sys

    eid = sys.argv[1]

    user = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(eid))
    tasks = requests.get("https://jsonplaceholder.typicode.com/todos/").json()
    etasks = []
    for task in tasks:
        userId = task.get('userId')
        if userId == int(eid):
            info = []
            info.append(eid)
            info.append(user.json().get('username'))
            info.append(str(task.get('completed')))
            info.append(task.get('title'))
            etasks.append(info)

    with open('{}.csv'.format(eid), 'w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        writer.writerows(etasks)
